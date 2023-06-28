from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import Dispatcher, types
from bot.database.methods.other import checkLogoPass
from bot.database.methods.create import create_user, get_yes_or_no, create_last_msg
from bot.database.methods.update import save_last_msg
from bot.database.models.users import Users
from bot.handlers.logoPass.otherFuncForLogopass import firstStartInputLogopass
from bot.keyboards.inline import inline_kbr_start, kbr_incorrect_logopass
from bot.misc.util import generationTextFirstBlood
from bot.startEndDay.actions.statusWork import getting_start


async def first_blood(call: Message, state: FSMContext) -> None:

    """
        Функция для 1‑го запуска
    """

    user_id = call.from_user.id
    await call.delete()
    # Пытаемся получить id юзера
    if not await get_yes_or_no(user_id):
        """ Создаются Записи, если отсутсвуют """
        await create_user(call)
        await create_last_msg(call)

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

            await call.answer(
                text=answerText,
                reply_markup=inline_kbr_start
            )
            await save_last_msg(call)

        else:
            # Если логопас не верен
            await call.answer(
                text='Неверно указан логин или пароль.',
                reply_markup=kbr_incorrect_logopass,
            )


async def echo(msg: Message, state: FSMContext) -> None:

    """
        Эхо функция
    """

    print('Я в эхо')
    await first_blood(msg, state)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'], state="*")
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY, state="*")


