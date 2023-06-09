from aiogram.dispatcher.filters.state import StatesGroup, State


class firstUse(StatesGroup):
    INPUT_LOGIN = State()
    INPUT_PASSWORD = State()