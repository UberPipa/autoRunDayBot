from bot.database.models.users import LastMsg, AutoManageDay


async def get_last_msg(call) -> int:
    """
    Receives the last message for the user.
    :param call:
    :return: int
    """

    # Устанавливаем определённого пользователя
    user = LastMsg.get(LastMsg.user_id == call.from_user.id)

    return user.msg_id


async def get_onOff_auto_manage_day_user_auto_stop(call) -> bool:
    """
    Receives the last message for the user.
    :param call:
    :return: bool
    """

    # Устанавливаем определённого пользователя
    user = AutoManageDay.get(AutoManageDay.user_id == call.from_user.id)
    auto_stop_status = user.auto_stop

    return auto_stop_status


async def get_auto_manage_day_user_current_status(call) -> bool:
    """
    Receives the last message for the user.
    :param call:
    :return: bool
    """

    # Устанавливаем определённого пользователя
    user = AutoManageDay.get(AutoManageDay.user_id == call.from_user.id)

    current_status = user.current_status

    return current_status
