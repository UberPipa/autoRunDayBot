import json

from bot.startEndDay.actions.other import reform_result
from bot.startEndDay.data import login, password, headers


async def close_day(session, csrf):
    """

        Функция закрывает рабочий день.

    """
    close = session.post(
        'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
        headers=headers,
        data={
            "timestamp": "0",
            "report": "",
            "device": "browser",
        },
        params={
            "action": "close",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = close.text.replace("'", "\"")
    status = json.loads(status)
    return status


async def reopen_day(session, csrf):
    """

        Функция переоткрывает рабочий день.

    """
    reopen = session.post(
        'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
        headers=headers,
        data={
            "timestamp": "0",
            "report": "",
            "device": "browser",
        },
        params={
            "action": "reopen",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = reopen.text.replace("'", "\"")
    status = json.loads(status)
    return status


async def pause_day(session, csrf):
    """

        Функция ставит на паузу рабочий день.

    """
    pause = session.post(
        'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
        headers=headers,
        data={
            "timestamp": "0",
            "report": "",
            "device": "browser",
        },
        params={
            "action": "pause",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = pause.text.replace("'", "\"")
    status = json.loads(status)
    return status


async def open_day(session, csrf):
    """

        Функция открывает рабочий день.

    """
    open = session.post(
        'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
        headers=headers,
        data={
            "timestamp": "0",
            "report": "",
            "device": "browser",
        },
        params={
            "action": "open",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = open.text.replace("'", "\"")
    status = json.loads(status)
    return status


async def forgot_day(session, csrf, close_time='0', report='ㅤ'):
    """

        Функция закрывает предыдущий рабочий день.
        !!! Если не передать время закрытия, то закрывает текущий день,
        отправляя невидимый символ.

    """
    close_last_day = session.post(
        "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
        data={
            "timestamp": close_time,
            "report": report,
            "device": "browser",
        },
        params={
            "action": "close",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = close_last_day.text.replace("'", "\"")
    status = json.loads(status)
    return status





# session, status, csrf = getting_start(login, password)
# reopen_day(session, csrf)




