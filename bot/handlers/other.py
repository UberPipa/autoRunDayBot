from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import Dispatcher, types, Bot

from bot.database.methods.other import checkLogoPass
from bot.keyboards.reply import startEnd_reply_kbr
from bot.database.methods.create import create_user, get_yes_or_no
from bot.misc.states import firstUse


async def first_blood(msg: Message, state: FSMContext) -> None:
    """ Функция для 1‑го запуска """
    user_id = msg.from_user.id
    await msg.delete()
    if not await get_yes_or_no(user_id):
        await create_user(int(user_id))
    # Проверяем на присутсвие логопаса
    if not await checkLogoPass(user_id):
        await state.set_state(firstUse.INPUT_LOGIN)
        await msg.answer(text='Введите ваш логин.')
    else:
        await msg.answer(text='Выберите кнопку:', reply_markup=startEnd_reply_kbr)


async def echo(msg: Message, state: FSMContext) -> None:
    """ Эхо функция """
    await first_blood(msg, state)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'], state="*")
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY, state="*")
