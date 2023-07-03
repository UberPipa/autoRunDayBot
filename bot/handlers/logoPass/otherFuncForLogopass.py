from aiogram import Bot

from bot.database.methods.get import get_last_msg
from bot.misc.states import firstUse
from aiogram.dispatcher import FSMContext
from aiogram import types


async def startInputLogopass(call: types.Message, state: FSMContext) -> None:
    """

    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot
    chat_id=call.from_user.id

    message_id = await get_last_msg(call)

    await bot.delete_message(chat_id=chat_id, message_id=message_id)

    # await bot.edit_message_reply_markup(
    #     chat_id=call.from_user.id,
    #     message_id=message_id,
    #     reply_markup=reply_markup
    # )

    await state.set_state(firstUse.INPUT_LOGIN)
    await bot.send_message(
        chat_id=chat_id,
        text='Введите ваш логин без "<code>@stdpr.ru</code>"'
    )


async def firstStartInputLogopass(call: types.Message, state: FSMContext) -> None:
    bot: Bot = call.bot
    chat_id = call.chat.id
    await state.set_state(firstUse.INPUT_LOGIN)
    await bot.send_message(
        chat_id=chat_id,
        text='Привет, я помогаю управлять рабочим днём.\n'
             'Сначала вам нужно авторизоваться.\n'
             'Введите ваш логин без "<code>@stdpr.ru</code>"'
    )