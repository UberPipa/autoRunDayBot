from aiogram.dispatcher import FSMContext
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup
from aiogram import Dispatcher, types, Bot
from bot.database.methods.other import checkLogoPass
from bot.handlers.other import first_blood
from bot.keyboards.reply import startEnd_reply_kbr
from bot.database.methods.create import create_user, get_yes_or_no
from bot.misc.states import firstUse
from bot.database.models.main import Users


async def inputLogin(msg: Message, state: FSMContext) -> None:
    """ Записывает в состоянии FSM логин """
    user = Users.get_by_id(msg.from_user.id)
    user.login = msg.text
    user.save()
    await state.finish()
    await state.set_state(firstUse.INPUT_PASSWORD)
    await msg.answer(text='Введите ваш пароль.')


async def inputPassword(msg: Message, state: FSMContext) -> None:
    """ Записывает в состоянии FSM пароль """
    user = Users.get_by_id(msg.from_user.id)
    user.password = msg.text
    user.save()
    await state.finish()
    await msg.answer(text='Выберите кнопку:', reply_markup=startEnd_reply_kbr)


async def changeLogopass(msg: Message, state: FSMContext) -> None:
    """ Команда для изменения логопаса """
    await state.set_state(firstUse.INPUT_LOGIN)
    await msg.answer(
        text='Введите ваш логин.',
        reply_markup=ReplyKeyboardMarkup().add(KeyboardButton(text="Отмена", resize_keyboard=True))
    )


async def cancel(msg: Message, state: FSMContext) -> None:
    """ Для кнопки отмены """
    await state.finish()
    await first_blood(msg, state)


def user_inputLogPass_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(inputLogin, state=firstUse.INPUT_LOGIN)
    dp.register_message_handler(inputPassword, state=firstUse.INPUT_PASSWORD)
    dp.register_message_handler(changeLogopass, commands=['chl', 'срд'], state="*")
    dp.register_message_handler(cancel, text='Отмена', state="*")
    pass