from aiogram import Dispatcher

from bot.handlers.admin import register_admin_handlers
from bot.handlers.logoPass.main import register_logopass_handlers
from bot.handlers.other import register_other_handlers
from bot.handlers.user import register_user_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers = (
        register_user_handlers,
        register_admin_handlers,
        register_logopass_handlers,
        register_other_handlers,

    )
    for handler in handlers:
        handler(dp)
