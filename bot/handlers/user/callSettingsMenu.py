from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.database.methods.get import get_last_msg, get_onOff_auto_manage_day_user_auto_stop
from bot.database.methods.update import switch_onOff_auto_manage_day_user_auto_stop


async def menuSettings(call: types.CallbackQuery) -> None:
    """
    Reference
    :param call: call
    :param state: FSMContext
    :return:
    """

    bot: Bot = call.bot

    # Edit last msg
    # Receives the last message for the user.

    i = await get_onOff_auto_manage_day_user_auto_stop(call)

    if not i:
        i = '✅'
    else:
        i = '❌'

    kbr_menuSettings = InlineKeyboardMarkup()
    kbr_menuSettings.add(InlineKeyboardButton(
        text=f'Авто завершение дня - {i}'.upper(),
        callback_data="autoStopDayNineHours")
    )
    kbr_menuSettings.add(InlineKeyboardButton(
        text='Сменить логопас'.upper(), callback_data="changeLogopass")
    )
    kbr_menuSettings.add(
        InlineKeyboardButton(text='Назад'.upper(), callback_data="statusDay")
    )

    message_id = await get_last_msg(call)
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=message_id,
        text='Меню настроек.',
        reply_markup=kbr_menuSettings
    )


async def switch_autoStopDay(call: types.CallbackQuery) -> None:
    """
    switches autostopDay and change msg
    :param call:
    :return:
    """

    bot: Bot = call.bot

    await switch_onOff_auto_manage_day_user_auto_stop(call)

    i = await get_onOff_auto_manage_day_user_auto_stop(call)

    if not i:
        await call.answer(text='Рабочий день будет завершаться принудительно в 21:00')

    if not i:
        i = '✅'
    else:
        i = '❌'

    kbr_menuSettings = InlineKeyboardMarkup()
    kbr_menuSettings.add(InlineKeyboardButton(
        text=f'Авто завершение дня - {i}'.upper(),
        callback_data="autoStopDayNineHours")
    )
    kbr_menuSettings.add(InlineKeyboardButton(
        text='Сменить логопас'.upper(), callback_data="changeLogopass")
    )
    kbr_menuSettings.add(
        InlineKeyboardButton(text='Назад'.upper(), callback_data="statusDay")
    )

    message_id = await get_last_msg(call)
    await bot.edit_message_text(
        chat_id=call.from_user.id,
        message_id=message_id,
        text='Меню настроек.',
        reply_markup=kbr_menuSettings
    )





def user_call_settings_menu_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(menuSettings, lambda call: call.data == 'settingDay')
    dp.register_callback_query_handler(switch_autoStopDay, lambda call: call.data == 'autoStopDayNineHours')
    pass



