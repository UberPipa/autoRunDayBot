from aiogram.types import Message
from aiogram import Dispatcher, types, Bot
from bot.keyboards.reply import startEnd_reply_kbr


async def first_blood(msg: Message) -> None:
    """ Функция для 1‑го запуска """
    print("Я в first_blood")
    bot: Bot = msg.bot
    await msg.delete()
    await msg.answer(text='Выберите кнопку:', reply_markup=startEnd_reply_kbr)


async def echo(msg: Message) -> None:
    """ Эхо функция """
    print("Я в echo")
    await msg.delete()


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'])
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY)
