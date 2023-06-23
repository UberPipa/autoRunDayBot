async def loginProcessing(msg) -> None:
    """
        Вызывает сообщение ввода логина, сделоно для приминения рекурсии
    """
    await msg.answer(
        text='Логин должен оканчиваться на "...<code>@stdpr.ru</code>"! Введите логин.'
    )
