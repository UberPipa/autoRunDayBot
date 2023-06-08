from bot.database.models.main import Users


async def get_user_by_id_or_none(user_id: int) -> Users | None:
    return Users.get_or_none(Users.user_id == user_id)


async def create_user(user_id: int) -> None:
    if not await get_user_by_id_or_none(user_id):
        Users.create(
            user_id=user_id,
            login=None,
            password=None
        )

