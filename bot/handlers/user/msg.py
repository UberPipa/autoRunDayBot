from aiogram import Dispatcher, types

from bot.database.methods.update import update_last_use
from bot.startEndDay.actions.actions import reopen_day, close_day, open_day
from bot.startEndDay.actions.statusWork import getting_start
from bot.database.models.users import Users
import datetime


async def openReopen_day(msg: types.Message) -> None:
    """

        Переоткрывает рабочий день. Пока только это!!!!!!!!!

    """
    user = Users.get_by_id(msg.from_user.id)
    login = user.login
    password = user.password
    update_last_use(msg)
    session, status, csrf = await getting_start(login, password)
    if status:
        if status['STATE'] == 'OPENED':
            await msg.answer(text='Рабочи день уже идёт')
        else:
            # Проверяем когда был последний старт дня, если сегодня, то применяем reopen, если нет, то open
            last_date_start = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
            last_date_start = last_date_start.date()
            today = datetime.date.today()
            if last_date_start == today:
                await reopen_day(session, csrf)
            else:
                await open_day(session, csrf)
            await msg.answer(text='Рабочий день начат')
    else:
        await msg.answer(text='Неверно указан логин или пароль')


async def closed_day(msg: types.Message) -> None:
    """

        Закрывает рабочий день

    """
    user = Users.get_by_id(msg.from_user.id)
    login = user.login
    password = user.password
    update_last_use(msg)
    session, status, csrf = await getting_start(login, password)
    if status:
        if status['STATE'] == 'CLOSED':
            await msg.answer(text='Рабочи день уже закрыт')
        else:
            await close_day(session, csrf)
            await msg.answer(text='Рабочий день закрыт')
    else:
        await msg.answer(text='Неверно указан логин или пароль.')


async def get_status(msg: types.Message) -> None:
    """

        Получает текущий статус

    """
    user = Users.get_by_id(msg.from_user.id)
    login = user.login
    password = user.password
    session, status, csrf = await getting_start(login, password)
    if status:
        status = status['STATE']
        await msg.answer(text=status)
    else:
        await msg.answer(text='Неверно указан логин или пароль')


def user_msg_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(openReopen_day, text='Начать день')
    dp.register_message_handler(closed_day, text="Завершить день")
    dp.register_message_handler(get_status, text='Узнать статус')
    pass
