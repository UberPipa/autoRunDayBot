import datetime
import time

from aiogram import types, Bot
from aiogram.utils.exceptions import MessageToEditNotFound, MessageToDeleteNotFound, MessageCantBeEdited, \
    MessageNotModified


async def generationTextFirstBlood(status) -> str:
    """

        Функция генерирует текст для шапки функции FirstBlood

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
        durationWork = f'Вы работаете: <code>{durationWork}</code>.\n'
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


async def delete_inline_and_msg(msg):
    """

        Удаление инлай клавиатуры и предыдущего сообщения

    """
    bot: Bot = msg.bot
    try:
        await msg.delete()  # удаляет сообщение от пользователя
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        # print("Сообщение для удаления не найдено")
        pass
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass
    chat_id = msg.chat.id
    message_id = msg.message_id - 1  # Идентификатор предыдущего сообщения
    reply_markup = types.InlineKeyboardMarkup()  # Создаем пустую клавиатуру
    try:
        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id,
                                            reply_markup=reply_markup)  # Отправляем отредактированное сообщение с пустой клавиатурой
    except MessageCantBeEdited:
        # print("Сообщение не может быть отредактировано")
        pass
    except MessageToEditNotFound:
        # print("Сообщение для редактирования не найдено")
        pass
    except MessageToDeleteNotFound:
        # print("Сообщение для удаления не найдено")
        pass
    except MessageNotModified:
        # print("Сообщение для удаления не найдено")
        pass


# async def generationTextStatus(status) -> str:
#     """
#
#         Функция генерирует текст статуса
#
#     """
#     state = status['STATE']
#     if state == 'OPENED':
#         state = 'Рабочий день <b>открыт</b> - 🟢.'
#     elif state == 'PAUSED':
#         state = 'Рабочий день <b>приостановлен</b> - ⏸️.'
#     elif state == 'CLOSED':
#         state = 'Рабочий день <b>закрыт</b> - 🛑.'
#     state = f'{state}\n'
#     text = state
#
#
#     if status['INFO']['DATE_START']:
#         """
#             Показывает дату и время начала рабочего дня
#         """
#         timeStart = datetime.datetime.fromtimestamp(int(status['INFO']['DATE_START']))
#         timeStart = f'День начат: <code>{timeStart}</code>.\n'
#         text += timeStart
#
#     if status['STATE'] == 'OPENED' or status['STATE'] == 'PAUSED':
#         """
#             Показывает рекомендуемое время завершения
#         """
#         timeStart = int(status['INFO']['DATE_START'])
#         nineHours = 32400
#         reccomendedTimeEndWork = datetime.datetime.fromtimestamp(timeStart + nineHours)
#         reccomendedTimeEndWork = f'Рекомендуемое время завершения+: <code>{reccomendedTimeEndWork}</code>.\n'
#         text += reccomendedTimeEndWork
#
#     return text