import json
from typing import Union
import requests
from bot.startEndDay.actions.other import check_auth
from bot.startEndDay.data import headers
from requests.exceptions import Timeout, ConnectionError, RequestException


async def getting_start(login, password) -> Union[object, dict, bool]:
    """
    Функция логинит пользователя, получает csrf токен и получает статус.
    После этой функции можно совершать действия с аккаунтом.
    :param login: from env
    :param password: from env
    :return: object | dict | bool
    """

    session = requests.Session()
    authorization = session.post(
        'https://bitrix.stdpr.ru',
        headers=headers,
        data={
            "AUTH_FORM": "Y",
            "TYPE": "AUTH",
            "backurl": "/auth/?backurl=%2Fstream%2F",
            f"USER_LOGIN": login,
            f"USER_PASSWORD": password,
        },
        params={
            "login": "yes",
            "backurl": "/stream/",
        }
    )

    result_auth = await check_auth(authorization)

    if result_auth:

        get_csrf = session.post(
            'https://bitrix.stdpr.ru/bitrix/services/main/ajax.php',
            headers=headers,
            params={
                "action": "bitrix:timeman.api.monitor.isAvailable",
            }
        )
        csrf = get_csrf.headers.get(
            'X-Bitrix-New-Csrf'
        )

        get_status = session.post(
            "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
            data={
                "device": "browser",
            },
            params={
                "action": "update",
                "site_id": "s1",
                "sessid": csrf,
            }
        )
        status = get_status.text.replace("'", "\"")
        status = json.loads(status)

        return session, status, csrf

    else:
        return False, False, False
