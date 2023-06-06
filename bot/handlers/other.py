from aiogram import Dispatcher
from aiogram.types import Message
from aiogram import Dispatcher, types

async def echo(msg: Message):
    """ Эхо функция """
    await msg.delete()


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(echo, content_types=types.ContentType.ANY)