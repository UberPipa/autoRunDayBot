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


    if status['INFO']['DATE_START'] and status['STATE'] == 'OPENED':
        """ 
            Показывает время работы 
        """
        timeStart = status['INFO']['DATE_START']
        # Текущее Unix время
        currentUnixTime = time.time()
        durationWork = int(currentUnixTime) - int(timeStart)
        durationWork = datetime.datetime.utcfromtimestamp(durationWork)
        durationWork = durationWork.strftime('%H:%M:%S')
        workTime = f'Вы уже работаете: <code>{durationWork}</code>.\n'
        text += workTime


    # state = status['STATE']
    # dateStart = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
    # if status['INFO']['DATE_FINISH']:
    #     dateFinish = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_FINISH']))
    # else:
    #     dateFinish = 0
    # duration = datetime.datetime.utcfromtimestamp(int(status['INFO']['DURATION']))
    # strDuration = duration.strftime('%H:%M:%S')
    #
    # # 9 часов - 32400; 8 - 28800
    # recommendedEnd = datetime.datetime.fromtimestamp(int((32400 - int(status['INFO']['DURATION'])) + int(time.time())))
    # recommendedEndStr = recommendedEnd.strftime('%H:%M:%S')
    # # recommendedEnd = recommendedEnd.strftime('%H:%M:%S')

    return text
