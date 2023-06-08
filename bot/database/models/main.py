from peewee import Model, SqliteDatabase, CharField

db = SqliteDatabase('users.db')


class _BaseModel(Model):
    class Meta:
        database = db


class Users(_BaseModel):
    user_id = CharField(unique=True, primary_key=True)
    chat_id = CharField(unique=True)
    login = CharField(max_length=50)
    password = CharField(max_length=50)


def register_models() -> None:
    for model in _BaseModel.__subclasses__():
        model.create_table()
