import datetime
import time


async def generationTextFirstBlood(status) -> str:
    """

        Функция генерирует текст для шапки функции FirstBlood

    """
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
    text = state

    if status['INFO']['DATE_START']:
        """ 
            Показывает время начала рабочего дня 
        """
        timeStart = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
        timeStart = timeStart.strftime('%H:%M:%S')
        timeStart = f'День начат: <code>{timeStart}</code>.\n'
        text += timeStart


    if status['INFO']['DATE_FINISH'] and status['STATE'] == 'CLOSED':
        """ 
            Показывает время завершения 
        """
        timeEnd = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_FINISH']))
        timeEnd = timeEnd.strftime('%H:%M:%S')
        timeEnd = f'Время завершения: <code>{timeEnd}</code>.\n'
        text += timeEnd


    if status['STATE'] == 'OPENED' or status['STATE'] == 'PAUSED':
        """ 
            Показывает время работы 
        """
        timeStart = status['INFO']['DATE_START']
        # Текущее Unix время
        currentUnixTime = time.time()
        durationWork = int(currentUnixTime) - int(timeStart)
        durationWork = datetime.datetime.utcfromtimestamp(durationWork)
        durationWork = durationWork.strftime('%H:%M:%S')
        durationWork = f'Вы уже работаете: <code>{durationWork}</code>.\n'
        text += durationWork


    if status['STATE'] == 'OPENED' or status['STATE'] == 'PAUSED':
        """ 
            Показывает рекомендуемое время завершения
        """
        timeStart = int(status['INFO']['DATE_START'])
        nineHours = 32400
        reccomendedTimeEndWork = datetime.datetime.fromtimestamp(timeStart + nineHours)
        reccomendedTimeEndWork = reccomendedTimeEndWork.strftime('%H:%M:%S')
        reccomendedTimeEndWork = f'Рекомендуем завершить в: <code>{reccomendedTimeEndWork}</code>.\n'
        text += reccomendedTimeEndWork


    if status['INFO']['DATE_FINISH'] and status['STATE'] == 'CLOSED' and status['INFO']['DATE_START']:
        """ 
            Показывает сколько всего проработал 
        """
        timeStart = int(status['INFO']['DATE_START'])
        timeEnd = int(status['INFO']['DATE_FINISH'])
        timeWork = timeEnd - timeStart
        timeWork = datetime.datetime.utcfromtimestamp(timeWork)
        timeWork = timeWork.strftime('%H:%M:%S')
        timeWork = f'Вы поработали: <code>{timeWork}</code>.\n'
        text += timeWork


    return text


async def generationTextStatus(status) -> str:
    """

        Функция генерирует текст для шапки функции FirstBlood

    """