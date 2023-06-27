from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kbr_start = InlineKeyboardMarkup()
""" Клавиатура для first_blood """
inline_kbr_start.add(InlineKeyboardButton(text='Начать работать'.upper(), callback_data="startDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Уйти на перерыв'.upper(), callback_data="pauseDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Завершить день'.upper(), callback_data="endDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Обновить статус'.upper(), callback_data="statusDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Настройки'.upper(), callback_data="settingDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Дополнительно'.upper(), callback_data="extraFeature"))
inline_kbr_start.add(InlineKeyboardButton(text='Справка'.upper(), callback_data="reference"))


kbr_incorrect_logopass = InlineKeyboardMarkup()
""" Клавиатура для смены логопаса """
kbr_incorrect_logopass.add(InlineKeyboardButton(text='Сменить логопас'.upper(), callback_data="changeLogopass"))