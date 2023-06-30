from aiogram import Dispatcher
from bot.handlers.user.callMainMenu import user_call_main_menu_handlers
from bot.handlers.user.callSettingsMenu import user_call_settings_menu_handlers


def register_user_handlers(dp: Dispatcher):
    user_call_main_menu_handlers(dp)
    user_call_settings_menu_handlers(dp)
    pass

