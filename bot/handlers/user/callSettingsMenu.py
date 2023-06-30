from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from bot.database.methods.get import get_last_msg
from bot.database.methods.update import update_last_use
from bot.keyboards.inline import inline_kbr_start
from bot.misc.states import inputTime
from bot.misc.util import checkCurrentDay, generationTextFirstBlood
from bot.startEndDay.actions.actions import reopen_day, close_day, open_day, pause_day
from bot.startEndDay.actions.statusWork import getting_start
from bot.database.models.users import Users
import datetime


# async def menuSettings(call: types.CallbackQuery, state: FSMContext) -> None:
#
#     """
#     Hunt a call to the settings menu and calls it
#     :param call:
#     :param state:
#     :return:
#     """
#
#     bot: Bot = call.bot
#
#     user = Users.get_by_id(call.from_user.id)
#     login = user.login
#     password = user.password
#
#     await update_last_use(call)
#
#     """ Стартуем сессию """
#     session, status, csrf = await getting_start(login, password)
#     if status:
#         if status['STATE'] == 'EXPIRED':
#             await state.set_state(inputTime.ENDAY)
#             await call.answer(text='Не завершён рабочий день, введите час(пока так) окончания рабочего дня. Формат 24 часа, 6 часов - это 6 утра!!!')
#         elif status['STATE'] == 'OPENED':
#             await call.answer(text='Рабочи день уже идёт')
#         else:
#             """ Проверяет когда был последний старт дня, если сегодня, то вернёт True, если нет, то False  """
#             if checkCurrentDay(status):
#                 await reopen_day(session, csrf)
#             else:
#                 await open_day(session, csrf)
#             await call.answer(text='Рабочий день начат')
#             # Edit last msg
#             # Receives the last message for the user.
#             message_id = await get_last_msg(call)
#             # get new status session
#             session, status, csrf = await getting_start(login, password)
#             # create new text
#             answerText = await generationTextFirstBlood(status)
#             # new answer text
#             await bot.edit_message_text(
#                 chat_id=call.from_user.id,
#                 message_id=message_id,
#                 text=answerText,
#                 reply_markup=inline_kbr_start
#             )
#     else:
#         await call.answer(
#             text='Неверно указан логин или пароль',
#         )

def user_call_settings_menu_handlers(dp: Dispatcher) -> None:
    # dp.register_callback_query_handler(menuSettings, lambda call: call.data == 'settingDay', state='*')

    pass