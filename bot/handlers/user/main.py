from aiogram import Dispatcher, types

from bot.handlers.user.msg import user_msg_handlers


def register_user_handlers(dp: Dispatcher):
    user_msg_handlers(dp)
    pass

