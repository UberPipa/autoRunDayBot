from aiogram.dispatcher.filters.state import StatesGroup, State


class firstUse(StatesGroup):
    INPUT_LOGIN = State()
    INPUT_PASSWORD = State()

class inputTime(StatesGroup):
    ENDAY = State()

class referenceMenu(StatesGroup):
    INMENU = State()
