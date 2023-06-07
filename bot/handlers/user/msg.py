from aiogram import Dispatcher, types, Bot
from bot.startEndDay.data import login, password
from bot.startEndDay.actions.actions import reopen_day, close_day
from bot.startEndDay.actions.statusWork import getting_start


async def startEnd_day(msg: types.Message) -> None:
    print("Я в startEnd_day")
    await msg.delete()
    if msg.text == 'Статус':
        session, status, csrf = await getting_start(login, password)
        STATE = status['STATE']
        await msg.answer(text=STATE)
        pass
    elif msg.text == 'Начать день':
        session, status, csrf = await getting_start(login, password)
        status = await reopen_day(session, csrf)

        print(status)
        print(type(status))
        #await msg.answer(text=STATE)
        #else:
            #await msg.answer(text='День начат!')
    elif msg.text == 'Завершить день':
        session, status, csrf = await getting_start(login, password)
        status = await close_day(session, csrf)
        print(status)
        print(type(status))


def user_msg_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(startEnd_day, text=['Начать день', 'Завершить день', 'Статус'])
    pass
