from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


startEnd_b1 = "Начать день"
startEnd_b2 = "Завершить день"
startEnd_b3 = "Узнать статус"
startEnd_b4 = "Сменить логопас"
startEnd_reply_kbr = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text=startEnd_b1),
            KeyboardButton(text=startEnd_b2)
        ],
        [
            KeyboardButton(text=startEnd_b3),
            KeyboardButton(text=startEnd_b4)
        ]
    ],
    resize_keyboard=True
)