from datetime import datetime
from typing import Union
from bot.database.models.main import Users


async def get_yes_or_no(user_id: int) -> Union[Users, None]:
    return Users.get_or_none(Users.user_id == user_id)


async def create_user(msg) -> None:
    user_id = msg.from_user.id
    if not await get_yes_or_no(user_id):
        Users.create(
            user_id=user_id,
            login=None,
            password=None,
            first_use=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            last_use=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            first_name=msg.from_user if "first_name" in msg.from_user else None,
            last_name=msg.from_user if "last_name" in msg.from_user else None,
            username=msg.from_user if "username" in msg.from_user else None,

        )
