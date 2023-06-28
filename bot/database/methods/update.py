from datetime import datetime

from bot.database.models.users import Users, LastMsg


async def update_last_use(call) -> None:

    """
        Фиксирует последнее использование бота
    """

    time_last_use = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Устанавливаем определённого пользователя
    user = Users.get(Users.user_id == call.from_user.id)

    user.last_use = time_last_use
    user.save()


async def update_last_msg(call) -> None:

    """
        Фиксирует id последнего сообщения
    """

    # Устанавливаем определённого пользователя
    user = LastMsg.get(LastMsg.user_id == call.from_user.id)

    user.msg_id = call.message_id
    user.save()
