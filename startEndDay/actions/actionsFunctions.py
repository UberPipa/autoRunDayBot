import os
from dotenv import load_dotenv
import requests
import fake_useragent
from startEndDay.actions.siteFunctions import login_user, check_status


def close_day():
    session = requests.Session()
    session, headers, status, csrf = check_status(session)

    ### Тут нужна проверка статуса перед выполнением

    params = {
        "timestamp": "0",
        "report": "",
        "device": "browser",
    }

    data = {
        "action": "close",
        "site_id": "s1",
        "sessid": csrf,
    }

    ### 3
    get_close = session.post(
        f'https://bitrix.stdpr.ru/bitrix/tools/timeman.php',
        headers=headers,
        params=params,
        data=data
    )
    print(get_close.text)


close_day()

