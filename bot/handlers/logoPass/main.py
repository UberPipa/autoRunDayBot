from aiogram import Dispatcher
from bot.handlers.logoPass.forLogoPass import user_inputLogPass_handlers


def register_user_handlers(dp: Dispatcher):
    user_inputLogPass_handlers(dp)
    pass

