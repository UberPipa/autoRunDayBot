from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from bot.database.methods.get import get_last_msg
from bot.database.methods.update import update_last_use, update_last_msg
from bot.keyboards.inline import inline_kbr_start, kbr_menuSettings
from bot.misc.states import inputTime
from bot.misc.util import checkCurrentDay, generationTextFirstBlood
from bot.startEndDay.actions.actions import reopen_day, close_day, open_day, pause_day
from bot.startEndDay.actions.statusWork import getting_start
from bot.database.models.users import Users
import datetime


async def menuSettings(call: types.CallbackQuery, state: FSMContext) -> None:

    """
    Reference
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    # Edit last msg
    # Receives the last message for the user.
    message_id = await get_last_msg(call)
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=message_id,
        text='Меню натсроек.',
        reply_markup=kbr_menuSettings
    )


def user_call_settings_menu_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(menuSettings, lambda call: call.data == 'settingDay', state='*')

    pass