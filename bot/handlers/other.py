from aiogram.types import Message
from aiogram import Dispatcher, types, Bot


async def first_blood(msg: Message) -> None:
    """ Функция для 1‑го запуска """
    print("Я в first_blood")
    bot: Bot = msg.bot
    await msg.delete()
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Начать день')
    button2 = types.KeyboardButton('Завершить день')
    button3 = types.KeyboardButton('Статус')
    keyboard.add(button1, button2, button3)
    await msg.answer(text='Выберите кнопку:', reply_markup=keyboard)


async def echo(msg: Message) -> None:
    """ Эхо функция """
    print("Я в echo")
    await msg.delete()


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'])
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY)
