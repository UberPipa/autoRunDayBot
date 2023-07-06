from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import Dispatcher, types, Bot
from aiogram.utils.exceptions import MessageNotModified

from bot.database.methods.get import get_last_msg
from bot.database.methods.other import checkLogoPass
from bot.database.methods.create import create_user, get_yes_or_no, create_last_msg_user, create_auto_manage_day_user
from bot.database.methods.update import update_last_msg
from bot.database.models.users import Users, LastMsg, AutoManageDay
from bot.handlers.logoPass.otherFuncForLogopass import firstStartInputLogopass
from bot.keyboards.inline import inline_kbr_start, kbr_incorrect_logopass, kbr_yankee_go_home, kbr_plug
from bot.misc.env import Admins
from bot.misc.states import referenceMenu
from bot.misc.util import generationTextFirstBlood
from bot.startEndDay.actions.statusWork import getting_start


async def first_blood(call: Message, state: FSMContext) -> None:
    """
    Функция для 1‑го запуска
    :param call: call
    :param state: FSMContext
    :return: None
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

    if not await get_yes_or_no(user_id, AutoManageDay):
        await create_auto_manage_day_user(call)

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


async def plug(call: types.CallbackQuery) -> None:
    """
    Menu for admins and change time
    :param call: call
    :param state: FSMContext
    :return: None
    """
    bot: Bot = call.bot

    admins = Admins.ADMINS.split(',')
    admins = tuple([int(i) for i in admins])

    if call.from_user.id in admins:
        # Edit last msg
        # Receives the last message for the user.
        message_id = await get_last_msg(call)
        await bot.edit_message_text(
            chat_id=call.from_user.id,
            message_id=message_id,
            text='Дополнительное меню.',
            reply_markup=kbr_plug
        )

    else:
        await call.answer(
            'Будем поделать.\n'
            'Разработчик короткий ножка.',
            show_alert=True
        )


async def reference(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Reference
    :param call: call
    :param state: FSMContext
    :return: None
    """

    bot: Bot = call.bot

    # Edit last msg
    # Receives the last message for the user.
    message_id = await get_last_msg(call)
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=message_id,
        text='v.0.85 (minor)\n'
             '- Бот полностью перенесён на инлайн кнопки\n'
             '- Появился учёт рабочего времени и рекомендуемое время завершения\n'
             '- Появилась возможность ставить рабочий день на паузу',
        reply_markup=kbr_yankee_go_home
    )


async def echo(msg: Message, state: FSMContext) -> None:
    """
    Eho
    :param msg: msg
    :param state: FSMContext
    :return: None
    """

    print('Я в эхо')
    print(msg)

    bot: Bot = msg.bot

    message_id = await get_last_msg(msg)
    reply_markup = types.InlineKeyboardMarkup()
    try:
        await bot.edit_message_reply_markup(
            chat_id=msg.from_user.id,
            message_id=message_id,
            reply_markup=reply_markup
        )
    except MessageNotModified:
        pass

    await first_blood(msg, state)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'], state="*")
    dp.register_callback_query_handler(plug, lambda call: call.data == 'plug')
    dp.register_callback_query_handler(reference, lambda call: call.data == 'reference', state='*')
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY, state="*")
