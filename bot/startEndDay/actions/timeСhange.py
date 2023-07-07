""""""
"""

        Функции нужно переписывать под асинхронность!!!

"""
""""""


from bot.startEndDay.actions.statusWork import getting_start


def change_startEnd_day(session, csrf, open_time, close_time, report='ㅤ') -> None:
    """

        Функция изменяет время начала и окончания рабочего дня.

    """
    close_last_day = session.post(
        "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
        data={
            "timeman_edit_from": open_time,
            "timeman_edit_to": close_time,
            "report": report,
            "device": "browser",
        },
        params={
            "action": "save",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = close_last_day.text


def change_start_day(session, csrf, open_time, report='ㅤ') -> None:
    """

        Функция изменяет время начала рабочего дня.

    """
    close_last_day = session.post(
        "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
        data={
            "timeman_edit_from": open_time,
            "report": report,
            "device": "browser",
        },
        params={
            "action": "save",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = close_last_day.text
    print(status)


def change_end_day(session, csrf, close_time, report='ㅤ') -> None:
    """

        Функция изменяет время окончания рабочего дня.

    """
    close_last_day = session.post(
        "https://bitrix.stdpr.ru/bitrix/tools/timeman.php",
        data={
            "timeman_edit_to": close_time,
            "report": report,
            "device": "browser",
        },
        params={
            "action": "save",
            "site_id": "s1",
            "sessid": csrf,
        }
    )
    status = close_last_day.text
    print(status)


# session, status, csrf = getting_start(login, password)
# change_startEnd_day(session, csrf, '36000', '64800')