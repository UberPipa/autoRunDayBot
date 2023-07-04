import os
from typing import Final
from dotenv import load_dotenv


class TgKeys:
    load_dotenv()
    TOKEN: Final = os.getenv('BOT_TOKEN')


class Admins:
    load_dotenv()
    ADMINS: Final = os.getenv('ADMINS')



