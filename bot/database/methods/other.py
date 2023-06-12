from bot.database.models.users import Users


async def checkLogoPass(user_id) -> bool:
    user = Users.get_by_id(user_id)
    if user.login is None or user.password is None:
        return False
    else:
        return True
