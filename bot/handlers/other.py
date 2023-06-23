import datetime
from aiogram.dispatcher import FSMContext
from aiogram.types import Message
from aiogram import Dispatcher, types
from bot.database.methods.other import checkLogoPass
from bot.database.methods.create import create_user, get_yes_or_no
from bot.database.models.users import Users
from bot.keyboards.inline import inline_kbr_start
from bot.misc.states import firstUse
from bot.startEndDay.actions.statusWork import getting_start


async def first_blood(call: Message, state: FSMContext) -> None:
    """ Функция для 1‑го запуска """
    user_id = call.from_user.id
    await call.delete()
    if not await get_yes_or_no(user_id):
        await create_user(call)
    # Проверяем на присутсвие логопаса
    if not await checkLogoPass(user_id):
        await state.set_state(firstUse.INPUT_LOGIN)
        await call.answer(text='Введите ваш логин.')
    else:
        user = Users.get_by_id(call.from_user.id)
        login = user.login
        password = user.password

        session, status, csrf = await getting_start(login, password)
        state = status['STATE']
        dateStart = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
        if status['INFO']['DATE_FINISH']:
            dateFinish = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_FINISH']))
        else:
            dateFinish = 0
        duration = datetime.datetime.utcfromtimestamp(int(status['INFO']['DURATION']))
        duration = duration.strftime('%H:%M:%S')


        await call.answer(
            text=f'Текущий статус - {state}\n'
                 f'Дата начала дня - {dateStart}\n'
                 f'Дата окончания дня - {dateFinish}\n'
                 f'Уже работаешь - {duration}\n'
                 f'{status}',
            reply_markup=inline_kbr_start
        )


async def echo(msg: Message, state: FSMContext) -> None:
    """ Эхо функция """
    await first_blood(msg, state)


def register_other_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(first_blood, commands=['start'], state="*")
    """ ЭХО ФУНКЦИЯ ВСЕГДА ДОЛЖНА БЫТЬ В САМОМ НИЗУ!!! """
    dp.register_message_handler(echo, content_types=types.ContentType.ANY, state="*")


