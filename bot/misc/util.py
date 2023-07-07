import datetime
import time

from aiogram import types, Bot
from aiogram.utils.exceptions import MessageToEditNotFound, MessageToDeleteNotFound, MessageCantBeEdited, \
    MessageNotModified


async def generationTextFirstBlood(status) -> str:
    """
    Функция генерирует текст для шапки функции FirstBlood
    :param status:
    :return:
    """

    nowTime = datetime.datetime.now()
    nowTime = nowTime.strftime('%Y-%m-%d %H:%M:%S')
    text = f'По состоянию на: <code>{nowTime}</code>.\n'

    state = status['STATE']
    if state == 'OPENED':
        state = '🟢'
    elif state == 'PAUSED':
        state = '⏸️'
    elif state == 'CLOSED':
        state = '🛑'
    elif state == 'EXPIRED':
        state = '❗️'
    state = f'Текущий статус: {state}\n'
    text += state

    if status['INFO']['DATE_START']:
        """ Проверяем когда был последний старт дня """

        if checkCurrentDay(status):

            timeStart = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
            timeStart = timeStart.strftime('%H:%M:%S')
            timeStart = f'День начат: <code>{timeStart}</code>.\n'
            text += timeStart

        else:
            timeStart = f'Сегодня рабочий день ещё не начат.\n'
            text += timeStart

    if status['INFO']['DATE_FINISH'] and status['STATE'] == 'CLOSED':
        """ Показывает время завершения """

        if checkCurrentDay(status):
            timeEnd = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_FINISH']))
            timeEnd = timeEnd.strftime('%H:%M:%S')
            timeEnd = f'Время завершения: <code>{timeEnd}</code>.\n'
            text += timeEnd

    if status['STATE'] == 'OPENED' or status['STATE'] == 'PAUSED':
        """ Показывает время работы """

        timeStart = status['INFO']['DATE_START']
        # Текущее Unix время
        currentUnixTime = time.time()
        durationWork = int(currentUnixTime) - int(timeStart)
        durationWork = datetime.datetime.utcfromtimestamp(durationWork)
        durationWork = durationWork.strftime('%H:%M:%S')
        durationWork = f'Вы работаете: <code>{durationWork}</code>.\n'
        text += durationWork

    if status['STATE'] == 'OPENED' or status['STATE'] == 'PAUSED':
        """ Показывает рекомендуемое время завершения """

        timeStart = int(status['INFO']['DATE_START'])
        nineHours = 32400
        reccomendedTimeEndWork = datetime.datetime.fromtimestamp(timeStart + nineHours)
        reccomendedTimeEndWork = reccomendedTimeEndWork.strftime('%H:%M:%S')
        reccomendedTimeEndWork = f'Рабочий день заканчивается в: <code>{reccomendedTimeEndWork}</code>.\n'
        text += reccomendedTimeEndWork

    if status['INFO']['DATE_FINISH'] and status['STATE'] == 'CLOSED' and status['INFO']['DATE_START']:
        """ Показывает сколько всего проработал """

        if checkCurrentDay(status):
            timeStart = int(status['INFO']['DATE_START'])
            timeEnd = int(status['INFO']['DATE_FINISH'])
            timeWork = timeEnd - timeStart
            timeWork = datetime.datetime.utcfromtimestamp(timeWork)
            timeWork = timeWork.strftime('%H:%M:%S')
            timeWork = f'Вы поработали: <code>{timeWork}</code>.\n'
            text += timeWork

    return text


def checkCurrentDay(status) -> bool:
    """
    Проверяет когда был последний старт дня, если сегодня, то вернёт True, если нет, то False
    :param status:
    :return:
    """

    last_date_start = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
    last_date_start = last_date_start.date()
    today = datetime.date.today()
    if last_date_start == today:
        return True
    else:
        return False


