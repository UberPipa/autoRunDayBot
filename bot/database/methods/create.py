from datetime import datetime
from typing import Union
from bot.database.models.users import Users


async def get_yes_or_no(user_id: int) -> Union[Users, None]:
    return Users.get_or_none(Users.user_id == user_id)


async def create_user(call) -> None:
    user_id = call.from_user.id
    if not await get_yes_or_no(user_id):
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


async def last_msg(call) -> None:
    user_id = call.from_user.id
    msg_id = call.message_id
    if not await get_yes_or_no(user_id):
        Users.create(
            user_id=user_id,
            msg_id=msg_id,

        )