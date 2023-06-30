from bot.database.models.users import LastMsg


async def get_last_msg(call) -> None:
    """
        Receives the last message for the user.
    """

    # Устанавливаем определённого пользователя
    user = LastMsg.get(LastMsg.user_id == call.from_user.id)

    print(user.msg_id)
    return user.msg_id
