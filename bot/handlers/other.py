from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import Dispatcher, types, Bot

from bot.database.methods.get import get_last_msg
from bot.database.methods.other import checkLogoPass
from bot.database.methods.create import create_user, get_yes_or_no, create_last_msg_user
from bot.database.methods.update import update_last_msg
from bot.database.models.users import Users, LastMsg
from bot.handlers.logoPass.otherFuncForLogopass import firstStartInputLogopass
from bot.keyboards.inline import inline_kbr_start, kbr_incorrect_logopass, kbr_yankee_go_home
from bot.misc.states import referenceMenu
from bot.misc.util import generationTextFirstBlood
from bot.startEndDay.actions.statusWork import getting_start


async def first_blood(call: Message, state: FSMContext) -> None:

    """
    Функция для 1‑го запуска
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    user_id = call.from_user.id
    await call.delete()
    # Пытаемся получить id юзера
    if not await get_yes_or_no(user_id, Users):
        """ Создаются таблицы, если отсутсвуют """
        await create_user(call)
    if not await get_yes_or_no(user_id, LastMsg):
        await create_last_msg_user(call)
    # Проверяем на присутсвие логопаса
    if not await checkLogoPass(user_id):
        # Eсли логопаса нет, запускаем функцию для ввода
        await firstStartInputLogopass(call, state)

    else:
        # Если всё ок и есть логопас, то получаем данные конкретного юзера
        user = Users.get_by_id(call.from_user.id)
        login = user.login
        password = user.password
        # Получаем сессию
        session, status, csrf = await getting_start(login, password)

        if status:
            # Если логопас верен генерируем текст
            answerText = await generationTextFirstBlood(status)

            await create_last_msg_user(call)

            sent_message = await bot.send_message(
                chat_id=call.chat.id,
                text=answerText,
                reply_markup=inline_kbr_start
            )

            # get id msg from bot
            message_id = sent_message.message_id
            await update_last_msg(call, message_id)


        else:
            # Если логопас не верен
            sent_message = await bot.send_message(
                chat_id=call.chat.id,
                text='Неверно указан логин или пароль.',
                reply_markup=kbr_incorrect_logopass,
            )

            message_id = sent_message.message_id
            await update_last_msg(call, message_id)


async def plug(call: types.CallbackQuery, state: FSMContext) -> None:

    """
    Загрушка для не реализованных call
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    await call.answer(
        'Будем поделать.\n'
        'Разработчик короткий ножка.',
        show_alert=True
    )


async def reference(call: types.CallbackQuery, state: FSMContext) -> None:

    """
    Reference
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    await state.set_state(referenceMenu.INMENU)
    # create empty keyboard
    reply_markup = types.InlineKeyboardMarkup()

    # Edit last msg
    # Receives the last message for the user.
    message_id = await get_last_msg(call)
    await bot.edit_message_reply_markup(
        chat_id=call.from_user.id,
        message_id=message_id,
        reply_markup=reply_markup
    )

    # sending a new message
    sent_message = await bot.send_message(
        chat_id=call.from_user.id,
        text='v.0.85 (minor)\n'
             '- Бот полностью перенесён на инлайн кнопки\n'
             '- Появился учёт рабочего времени и рекомендуемое время завершения\n'
             '- Появилась возможность ставить рабочий день на паузу',
        reply_markup=kbr_yankee_go_home
    )

    # get id msg from bot
    message_id = sent_message.message_id
    await update_last_msg(call, message_id)


async def echo(msg: Message, state: FSMContext) -> None:

    """
    Eho
    :param msg:
    :param state:
    :return:
    """

    print('Я в эхо')
    bot: Bot = msg.bot
    chat_id = msg.chat.id
    message_id = await get_last_msg(msg)
    await bot.delete_message(chat_id=chat_id, message_id=message_id)
    await first_blood(msg, state)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'], state="*")
    dp.register_callback_query_handler(plug, lambda call: call.data == 'plug', state='*')
    dp.register_callback_query_handler(reference, lambda call: call.data == 'reference', state='*')
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY, state="*")
