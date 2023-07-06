from datetime import datetime
from bot.database.methods.create import get_yes_or_no
from bot.database.models.users import Users, LastMsg, AutoManageDay
from bot.database.other import checkCurrentStatus


async def update_last_use(call) -> None:
    """
    Фиксирует последнее использование бота
    :param call:
    :return:
    """

    time_last_use = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Устанавливаем определённого пользователя
    user = Users.get(Users.user_id == call.from_user.id)

    user.last_use = time_last_use
    user.save()


async def update_last_msg(call, message_id) -> None:
    """
    Фиксирует id последнего сообщения
    :param call:
    :param message_id:
    :return:
    """

    # Устанавливаем определённого пользователя
    user = LastMsg.get(LastMsg.user_id == call.from_user.id)

    user.msg_id = message_id
    user.save()


async def switch_onOff_auto_manage_day_user_auto_stop(call) -> None:
    """
    On/off auto_stop
    :param call:
    :return:
    """

    # Устанавливаем определённого пользователя
    user = AutoManageDay.get(AutoManageDay.user_id == call.from_user.id)

    if user.auto_stop:
        user.auto_stop = False
    else:
        user.auto_stop = True

    user.save()


# async def update_auto_manage_day_user_current_status(call) -> None:
#     """
#     update current_status
#     :param call:
#     :return:
#     """
#
#     # Устанавливаем определённого пользователя
#     user = AutoManageDay.get(AutoManageDay.user_id == call.from_user.id)
#
#     status =
#     await checkCurrentStatus(status)
#     user.current_status =
#
#     user.save()
