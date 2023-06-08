import json
from typing import Union


async def check_auth(authorization) -> Union[bool]:
    """

        Функция проверяет пользователя на авторизацию.

    """
    result_auth = authorization.text.find('Неверный логин')
    if result_auth <= 0:
        return True
    else:
        return False

