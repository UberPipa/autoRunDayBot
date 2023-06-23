import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import Dispatcher

from bot.handlers.logoPass.otherFuncLogoPass import loginProcessing
from bot.handlers.other import first_blood
from bot.keyboards.reply import startEnd_reply_kbr
from bot.misc.states import firstUse, inputTime
from bot.database.models.users import Users
from bot.startEndDay.actions.actions import forgot_day
from bot.startEndDay.actions.statusWork import getting_start


async def inputLogin(msg: Message, state: FSMContext) -> None:
    """
        Записывает в состоянии FSM логин
    """
    text = msg.text

    if re.search(
            '@stdpr\.ru',
            text
    ):

        user = Users.get_by_id(msg.from_user.id)
        user.login = msg.text
        user.save()
        await state.finish()
        await state.set_state(firstUse.INPUT_PASSWORD)

        await msg.answer(
            text='Введите ваш пароль.'
        )

    else:
        await loginProcessing(msg)


async def inputPassword(msg: Message, state: FSMContext) -> None:
    """ Записывает в состоянии FSM пароль """
    user = Users.get_by_id(msg.from_user.id)
    user.password = msg.text
    user.save()
    await state.finish()
    await first_blood(msg, state)


async def changeLogopass(msg: Message, state: FSMContext) -> None:
    """ Команда для изменения логопаса """
    await state.set_state(firstUse.INPUT_LOGIN)
    await msg.answer(
        text='Сбросить логопас'
    )


async def cancel(msg: Message, state: FSMContext) -> None:
    """ Для кнопки отмены """
    await state.finish()
    await first_blood(msg, state)


async def endEXPIREDday(msg: Message, state: FSMContext) -> None:
    """ Функция завершает рабочий день, котоырй забыли завкрыть """
    try:
        hour = int(msg.text)
        await msg.answer(text=f'Ок, день завершёл в {hour}')
        user = Users.get_by_id(msg.from_user.id)
        login = user.login
        password = user.password
        session, status, csrf = await getting_start(login, password)
        await forgot_day(session, csrf, str(hour * 3600))
        await state.finish()
    except:
        await msg.answer(text=f'Ещё раз, не разобрал...')


def user_inputLogPass_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(inputLogin, state=firstUse.INPUT_LOGIN)
    dp.register_message_handler(inputPassword, state=firstUse.INPUT_PASSWORD)
    dp.register_message_handler(changeLogopass, text=['Сменить логопас'], state="*")
    dp.register_message_handler(cancel, text='Отмена', state="*")
    dp.register_message_handler(endEXPIREDday, content_types=types.ContentType.TEXT, state=inputTime.ENDAY)
    pass