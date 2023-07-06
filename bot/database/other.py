

async def checkCurrentStatus(status) -> bool:
    """
    Проверяет текущий статус работы
    :param status: status
    :return: bool
    """

    state = status['STATE']
    if state == 'OPENED':
        state = True

    elif state == 'PAUSED':
        state = True

    elif state == 'CLOSED':
        state = False

    elif state == 'EXPIRED':
        state = False

    return state