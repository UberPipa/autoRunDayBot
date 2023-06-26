import os
from peewee import Model, SqliteDatabase, CharField, IntegerField


db_folder = 'db'
if not os.path.exists(db_folder):
    os.makedirs(db_folder)
db = SqliteDatabase(os.path.join(db_folder, 'users.db'))


class BaseModel(Model):
    class Meta:
        database = db


class Users(BaseModel):
    user_id = IntegerField(unique=True, primary_key=True)
    login = CharField(max_length=50, null=True)
    password = CharField(max_length=50, null=True)
    first_use = CharField(max_length=50, null=True)
    last_use = CharField(max_length=50, null=True)
    first_name = CharField(max_length=50, null=True)
    last_name = CharField(max_length=50, null=True)
    username = CharField(max_length=50, null=True)


class LastMsg(BaseModel):
    user_id = IntegerField(unique=True, primary_key=True)
    msg_id = CharField(max_length=50, null=True)


def register_models() -> None:
    for model in BaseModel.__subclasses__():
        model.create_table()
