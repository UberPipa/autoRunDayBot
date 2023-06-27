from aiogram import Dispatcher
from bot.handlers.logoPass.forLogoPass import user_all_handlers


def register_logopass_handlers(dp: Dispatcher):
    user_all_handlers(dp)
    pass

