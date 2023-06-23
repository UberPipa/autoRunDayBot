from aiogram import Dispatcher
from bot.handlers.user.call import user_call_handlers


def register_user_handlers(dp: Dispatcher):
    user_call_handlers(dp)
    pass

