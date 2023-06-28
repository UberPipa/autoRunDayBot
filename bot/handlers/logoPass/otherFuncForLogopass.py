from aiogram import Bot
from bot.misc.states import firstUse
from aiogram.dispatcher import FSMContext
from aiogram.types import Message


async def startInputLogopass(call: Message, state: FSMContext) -> None:
    bot: Bot = call.bot
    chat_id = call.chat.id
    await state.set_state(firstUse.INPUT_LOGIN)
    await bot.send_message(
        chat_id=chat_id,
        text='Введите ваш логин без "<code>@stdpr.ru</code>"'
    )


async def firstStartInputLogopass(call: Message, state: FSMContext) -> None:
    bot: Bot = call.bot
    chat_id = call.chat.id
    await state.set_state(firstUse.INPUT_LOGIN)
    await bot.send_message(
        chat_id=chat_id,
        text='Привет, я помогаю управлять рабочим днём.\n'
             'Сначала вам нужно авторизоваться,\n'
             'введите ваш логин без "<code>@stdpr.ru</code>"'
    )