from aiogram import Dispatcher, types
from bot.startEndDay.data import login, password
from bot.startEndDay.actions.actions import reopen_day, close_day
from bot.startEndDay.actions.statusWork import getting_start


async def openReopen_day(msg: types.Message) -> None:
    """

        Переоткрывает рабочий день

    """
    session, status, csrf = await getting_start(login, password)
    if status:
        if status['STATE'] == 'OPENED':
            await msg.answer(text='Рабочи день уже идёт')
        else:
            await reopen_day(session, csrf)
            await msg.answer(text='Рабочий день начат')
    else:
        await msg.answer(text='Неверно указан логин или пароль')


async def closed_day(msg: types.Message) -> None:
    """

        Закрывает рабочий день

    """
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
