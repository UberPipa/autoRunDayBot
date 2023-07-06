from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from bot.database.methods.get import get_last_msg
from bot.keyboards.inline import kbr_menuSettings



async def menuSettings(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Reference
    :param call: call
    :param state: FSMContext
    :return:
    """

    bot: Bot = call.bot

    # Edit last msg
    # Receives the last message for the user.
    message_id = await get_last_msg(call)
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=message_id,
        text='Меню настроек.',
        reply_markup=kbr_menuSettings
    )


def user_call_settings_menu_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(menuSettings, lambda call: call.data == 'settingDay', state='*')

    pass