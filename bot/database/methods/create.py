from datetime import datetime
from typing import Union
from bot.database.models.users import Users, LastMsg, AutoManageDay


async def get_yes_or_no(user_id: int, db) -> Union[Users, None]:
    """
    Ищет юзера в базе, возвращент его id или None
    :param user_id:
    :return: Users, None
    """

    return db.get_or_none(db.user_id == user_id)


async def create_user(call) -> None:
    """
    Создаёт юзера в сущности users
    :param call:
    :return: None
    """

    user_id = call.from_user.id
    if not await get_yes_or_no(user_id, Users):
        Users.create(
            user_id=user_id,
            login=None,
            password=None,
            first_use=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            last_use=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            first_name=call.from_user['first_name'] if "first_name" in call.from_user else None,
            last_name=call.from_user['last_name'] if "last_name" in call.from_user else None,
            username=call.from_user['username'] if "username" in call.from_user else None,

        )


async def create_last_msg_user(call) -> None:
    """
    Создаёт юзера в сущности LastMsg
    :param call:
    :return: None
    """

    user_id = call.from_user.id
    msg_id = call.message_id
    if not await get_yes_or_no(user_id, LastMsg):
        LastMsg.create(
            user_id=user_id,
            msg_id=msg_id,

        )


async def create_auto_manage_day_user(call) -> None:
    """
    Создаёт юзера в сущности AutoManageDay
    :param call:
    :return: None
    """

    user_id = call.from_user.id
    if not await get_yes_or_no(user_id, AutoManageDay):
        AutoManageDay.create(
            user_id=user_id,
            auto_stop=False,
            current_status=None,

        )
