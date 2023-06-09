from aiogram import Dispatcher
from bot.handlers.user.forLogoPass import user_inputLogPass_handlers
from bot.handlers.user.msg import user_msg_handlers


def register_user_handlers(dp: Dispatcher):
    user_msg_handlers(dp)
    user_inputLogPass_handlers(dp)
    pass

