from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

inline_kbr_start = InlineKeyboardMarkup()
""" Клавиатура для first_blood """
inline_kbr_start.add(InlineKeyboardButton(text='Начать работать'.upper(), callback_data="startDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Уйти на перерыв'.upper(), callback_data="pauseDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Завершить день'.upper(), callback_data="endDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Обновить статус'.upper(), callback_data="statusDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Настройки'.upper(), callback_data="settingDay"))
inline_kbr_start.add(InlineKeyboardButton(text='Дополнительно'.upper(), callback_data="plug"))
inline_kbr_start.add(InlineKeyboardButton(text='Справка'.upper(), callback_data="reference"))


kbr_incorrect_logopass = InlineKeyboardMarkup()
""" Клавиатура для смены логопаса """
kbr_incorrect_logopass.add(InlineKeyboardButton(text='Сменить логопас'.upper(), callback_data="changeLogopass"))


kbr_yankee_go_home = InlineKeyboardMarkup()
""" кнопка назад """
kbr_yankee_go_home.add(InlineKeyboardButton(text='Назад'.upper(), callback_data="statusDay"))


kbr_plug = InlineKeyboardMarkup()
""" Клавиатура для доп. меню """
kbr_plug.add(InlineKeyboardButton(text='Выгрузить БД'.upper(), callback_data="unloadingDB"))
kbr_plug.add(InlineKeyboardButton(text='Назад'.upper(), callback_data="statusDay"))
#kbr_plug.add(InlineKeyboardButton(text='Выгрузить Логи'.upper(), callback_data="autoStopDayNineHours"))


kbr_chek = InlineKeyboardMarkup()
""" Клавиатура при отсутсвии интернета или отвала битрикса """
kbr_chek.add(InlineKeyboardButton(text='Проверить соединение'.upper(), callback_data="statusDay"))
