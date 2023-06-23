from datetime import datetime

from bot.database.models.users import Users


def update_last_use(call):
    time_last_use = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    user = Users.get(Users.user_id == call.from_user.id)
    user.last_use = time_last_use
    user.save()
