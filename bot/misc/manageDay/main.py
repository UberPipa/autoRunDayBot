# import asyncio
# from aiogram.dispatcher import Dispatcher
# from aioschedule import every, run_pending
#
#
# async def send_message(dp: Dispatcher):
#     # Отправляем сообщение
#     bot: dp.bot
#     message = "Привет, мир!"
#     await bot.send_message(1285846225, message)
#
# def start_scheduler():
#     # Запускаем планировщик задач
#     loop = asyncio.get_event_loop()
#     loop.create_task(schedule_messages)
#     loop.run_forever()
#
#
# async def schedule_messages():
#     # Запускаем цикл отправки сообщений каждые 10 секунд
#     while True:
#         every(10).seconds.do(send_message)
#         await asyncio.sleep(10)
#         run_pending()
#
#
# def register_tasks(dp: Dispatcher) -> None:
#     tasks = (
#         start_scheduler()
#     )
#     for handler in tasks:
#         handler(dp)