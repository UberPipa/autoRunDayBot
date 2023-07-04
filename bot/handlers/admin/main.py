from aiogram import Dispatcher
from bot.handlers.admin.callMenuPlag import admin_call_plag_menu_handlers


def register_admin_handlers(dp: Dispatcher):
    admin_call_plag_menu_handlers(dp)
    pass
