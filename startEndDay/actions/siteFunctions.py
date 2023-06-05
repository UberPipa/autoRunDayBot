import os
from typing import Union
from dotenv import load_dotenv
import requests
import fake_useragent


def login_user(session) -> Union[object, dict]:
    """

         Функция только логинит логинит пользователя.

    """
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    user = fake_useragent.UserAgent().random
    headers = {
        'User-Agent': user,
    }
    session.post(
        'https://bitrix.stdpr.ru/?login=yes',
        headers=headers,
        data={
            "AUTH_FORM": "Y",
            "TYPE": "AUTH",
            "backurl": "/",
            f"USER_LOGIN": login,
            f"USER_PASSWORD": password,
        }
    )
    return session, headers


def get_status(session) -> Union[object, dict]:
    """

         Функция логинит пользователя, получает csrf токен и получает статус.
         После этой функции можно совершать дейтсвия с аккаунтом.

    """
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    user = fake_useragent.UserAgent().random
    headers = {
        'User-Agent': user,
    }

    data = {
        "AUTH_FORM": "Y",
        "TYPE": "AUTH",
        "backurl": "/",
        f"USER_LOGIN": login,
        f"USER_PASSWORD": password,
    }

    session.post(
        'https://bitrix.stdpr.ru/?login=yes',
        headers=headers,
        data={
            "AUTH_FORM": "Y",
            "TYPE": "AUTH",
            "backurl": "/",
            f"USER_LOGIN": login,
            f"USER_PASSWORD": password,
        }
    )

    get_csrf = session.post(
        'https://bitrix.stdpr.ru/bitrix/services/main/ajax.php?action=bitrix%3Atimeman.api.monitor.isAvailable',
        headers=headers
    )
    csrf = get_csrf.headers.get(
        'X-Bitrix-New-Csrf'
    )

    get_update = session.post(
        "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
        data={
            "action": "update",
            "site_id": "s1",
            "sessid": csrf,
        },
        params={
            "device": "browser",
        }
    )

    status = get_update.text
    return session, headers, status, csrf
