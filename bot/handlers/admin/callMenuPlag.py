import os
import sqlite3
from pydoc import locate
from aiogram import Dispatcher, types, Bot
from aiogram.dispatcher import FSMContext
from bot.database.methods.get import get_last_msg
from bot.database.methods.update import update_last_use, update_last_msg
from bot.keyboards.inline import inline_kbr_start, kbr_menuSettings
from bot.misc.states import inputTime
from bot.misc.util import checkCurrentDay, generationTextFirstBlood
from bot.startEndDay.actions.actions import reopen_day, close_day, open_day, pause_day
from bot.startEndDay.actions.statusWork import getting_start
from bot.database.models.users import Users, db_folder
import datetime


async def unloadingDB(call: types.CallbackQuery) -> None:
    """
    For admins functions
    :param call: call
    :param state: FSMContext
    :return:
    """

    bot: Bot = call.bot

    entry_point_path = os.path.abspath('main.py')
    mainDir = os.path.abspath(os.path.join(entry_point_path, '..'))
    db_locate = os.path.join(mainDir, 'db', 'database.db')

    db = types.InputFile(db_locate)

    await bot.send_document(
        chat_id=call.message.chat.id,
        document=db
    )

    report_locate = os.path.join(mainDir, 'tmp', 'database.txt')

    conn = sqlite3.connect(db_locate)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    # create list
    data = cursor.fetchall()
    print(data)
    with open(report_locate, 'w') as f:
        # записываем заголовки
        headers = "('user_id', 'login', 'password', 'first_use', 'last_use', 'first_name', 'last_name', 'username')\n"
        f.write(headers)
        for row in data:
            f.write(str(row) + '\n')

    report_locate = types.InputFile(report_locate)
    await bot.send_document(
        chat_id=call.message.chat.id,
        document=report_locate
    )


def admin_call_plag_menu_handlers(dp: Dispatcher) -> None:
    dp.register_callback_query_handler(unloadingDB, lambda call: call.data == 'unloadingDB')
    pass
