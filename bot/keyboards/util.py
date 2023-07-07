from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.database.methods.get import get_onOff_auto_manage_day_user_auto_stop


async def get_kbr_menuSettings(call) -> InlineKeyboardMarkup:
    """
    Generates a keyboard
    :param call:
    :return: object
    """

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

    return kbr_menuSettings
