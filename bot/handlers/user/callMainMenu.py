from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from bot.database.methods.get import get_last_msg
from bot.database.methods.update import update_last_use, update_last_msg
from bot.keyboards.inline import inline_kbr_start
from bot.misc.states import inputTime
from bot.misc.util import checkCurrentDay, generationTextFirstBlood
from bot.startEndDay.actions.actions import reopen_day, close_day, open_day, pause_day
from bot.startEndDay.actions.statusWork import getting_start
from bot.database.models.users import Users
import datetime
from aiogram.dispatcher.filters.state import State


async def openReopen_day(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Переоткрывает рабочий день.
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    user = Users.get_by_id(call.from_user.id)
    login = user.login
    password = user.password

    await update_last_use(call)

    """ Стартуем сессию """
    session, status, csrf = await getting_start(login, password)
    if status:
        if status['STATE'] == 'EXPIRED':
            await state.set_state(inputTime.ENDAY)
            await call.answer(text='Не завершён рабочий день, введите час(пока так) окончания рабочего дня. Формат 24 часа, 6 часов - это 6 утра!!!')
        elif status['STATE'] == 'OPENED':
            await call.answer(text='Рабочи день уже идёт')
        else:
            """ Проверяет когда был последний старт дня, если сегодня, то вернёт True, если нет, то False  """
            if checkCurrentDay(status):
                # if opened today, edit last msg
                await reopen_day(session, csrf)
                await call.answer(text='Рабочий день начат')
                # Edit last msg
                # Receives the last message for the user.
                message_id = await get_last_msg(call)
                # get new status session
                session, status, csrf = await getting_start(login, password)
                # create new text
                answerText = await generationTextFirstBlood(status)
                # new answer text
                await bot.edit_message_text(
                    chat_id=call.from_user.id,
                    message_id=message_id,
                    text=answerText,
                    reply_markup=inline_kbr_start
                )

            else:
                # if Yesterday, send new msg
                await open_day(session, csrf)

                message_id = await get_last_msg(call)
                # create new text
                reply_markup = types.InlineKeyboardMarkup()

                await bot.edit_message_reply_markup(
                    chat_id=call.from_user.id,
                    message_id=message_id,
                    reply_markup=reply_markup
                )

                # get new status session
                session, status, csrf = await getting_start(login, password)
                answerText = await generationTextFirstBlood(status)

                sent_message = await bot.send_message(
                    chat_id=call.from_user.id,
                    text=answerText,
                    reply_markup=inline_kbr_start
                )

                # get id msg from bot
                message_id = sent_message.message_id
                # save last msg
                await update_last_msg(call, message_id)

    else:
        await call.answer(
            text='Неверно указан логин или пароль',
        )


async def closed_day(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Закрывает рабочий день
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    user = Users.get_by_id(call.from_user.id)
    login = user.login
    password = user.password

    # fixing the usage
    await update_last_use(call)

    session, status, csrf = await getting_start(login, password)
    if status:
        if status['STATE'] == 'EXPIRED':
            await state.set_state(inputTime.ENDAY)
            await call.answer(text='Не завершён рабочий день, введите час(пока так) окончания рабочего дня. Формат 24 часа, 6 часов - это 6 утра!!!')
        elif status['STATE'] == 'CLOSED':
            await call.answer(text='Рабочи день уже закрыт')
        else:
            await close_day(session, csrf)
            await call.answer(text='Рабочий день закрыт')

            # Edit last msg
            # Receives the last message for the user.
            message_id = await get_last_msg(call)
            # get new status session
            session, status, csrf = await getting_start(login, password)
            # create new text
            answerText = await generationTextFirstBlood(status)
            # new answer text
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=message_id,
                text=answerText,
                reply_markup=inline_kbr_start
            )

    else:
        await call.answer(
            text='Неверно указан логин или пароль.',
        )


async def coffeBreak_day(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Ставит на паузу рабочий день.
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot

    user = Users.get_by_id(call.from_user.id)
    login = user.login
    password = user.password

    await update_last_use(call)

    session, status, csrf = await getting_start(login, password)
    if status:
        if status['STATE'] == 'EXPIRED':
            await state.set_state(inputTime.ENDAY)
            await call.answer(text='Не завершён рабочий день, введите час(пока так) окончания рабочего дня. Формат 24 часа, 6 часов - это 6 утра!!!')
        elif status['STATE'] == 'PAUSED':
            await call.answer(text='Рабочи день уже приостановлен')
        elif status['STATE'] == 'CLOSED':
            """ 
                Если мы нажимаем на паузу во время закрытого дня.
                Проверяем когда был последний старт дня, если сегодня, то применяем reopen, если нет, то open,
                Затем ставим день на паузу
            """
            if checkCurrentDay(status):
                await reopen_day(session, csrf)
            else:
                await open_day(session, csrf)
            await pause_day(session, csrf)

            # Edit last msg
            # Receives the last message for the user.
            message_id = await get_last_msg(call)
            # get new status session
            session, status, csrf = await getting_start(login, password)
            # create new text
            answerText = await generationTextFirstBlood(status)
            # new answer text
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=message_id,
                text=answerText,
                reply_markup=inline_kbr_start
            )

            await call.answer(text='Рабочий день приостановлен')

        else:

            await pause_day(session, csrf)

            # Edit last msg
            # Receives the last message for the user.
            message_id = await get_last_msg(call)
            # get new status session
            session, status, csrf = await getting_start(login, password)
            # create new text
            answerText = await generationTextFirstBlood(status)
            # new answer text
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=message_id,
                text=answerText,
                reply_markup=inline_kbr_start
            )

            await call.answer(text='Рабочий день приостановлен')

    else:
        await call.answer(
            text='Неверно указан логин или пароль.'
        )



async def get_status(call: types.CallbackQuery, state: FSMContext) -> None:
    """
    Получает текущий статус
    :param call:
    :param state:
    :return:
    """

    bot: Bot = call.bot
    user = Users.get_by_id(call.from_user.id)
    login = user.login
    password = user.password

    await update_last_use(call)

    session, status, csrf = await getting_start(login, password)

    if status:

        if status['STATE'] == 'EXPIRED':

            await state.set_state(inputTime.ENDAY)
            await call.answer(text='Не завершён рабочий день, введите час(пока так) окончания рабочего дня. Формат 24 часа, 6 часов - это 6 утра!!!')
            status = status['STATE']
            await call.answer(text=status)

        else:

            # Edit last msg
            # Receives the last message for the user.
            message_id = await get_last_msg(call)
            # create new text
            answerText = await generationTextFirstBlood(status)
            # new answer text
            await bot.edit_message_text(
                chat_id=call.from_user.id,
                message_id=message_id,
                text=answerText,
                reply_markup=inline_kbr_start
            )

    else:
        await call.answer(text='Неверно указан логин или пароль')


def user_call_main_menu_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(openReopen_day, lambda call: call.data == 'startDay', state='*')
    dp.register_callback_query_handler(closed_day, lambda call: call.data =="endDay", state='*')
    dp.register_callback_query_handler(coffeBreak_day, lambda call: call.data == "pauseDay", state='*')
    dp.register_callback_query_handler(get_status, lambda call: call.data == "statusDay", state='*')
    pass
