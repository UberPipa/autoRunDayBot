from aiogram import Dispatcher, types, Bot

from bot.keyboards.reply import startEnd_b1, startEnd_b2, startEnd_b3
from bot.startEndDay.data import login, password
from bot.startEndDay.actions.actions import reopen_day, close_day
from bot.startEndDay.actions.statusWork import getting_start


async def openReopen_day(msg: types.Message) -> None:
    session, status, csrf = await getting_start(login, password)
    if status:
        status = await reopen_day(session, csrf)
        print(status)
        print(type(status))


async def closed_day(msg: types.Message) -> None:
    session, status, csrf = await getting_start(login, password)
    status = await close_day(session, csrf)
    print(status)
    print(type(status))


async def get_status(msg: types.Message) -> None:
    session, status, csrf = await getting_start(login, password)
    print(status)
    print(type(status))






def user_msg_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(openReopen_day, text='Начать день')
    dp.register_message_handler(closed_day, text="Завершить день")
    dp.register_message_handler(get_status, text='Узнать статус')
    pass
