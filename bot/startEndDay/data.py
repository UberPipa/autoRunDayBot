import fake_useragent


user = fake_useragent.UserAgent().random
headers = {
    'User-Agent': user,
}


# {
#   "ID": "52118",
#   "STATE": "CLOSED",              # Текущий статус
#   "CAN_EDIT": "Y",
#   "CAN_OPEN": "REOPEN",           # Предположительно, что может быть сделано со статусом
#   "REPORT_REQ": "A",
#   "TM_FREE": false,
#   "INFO": {
#     "DATE_START": "1686027000",   # Дата старта - 06.06.2023, 07:50:00
#     "DATE_FINISH": "1686060000",  # Дата окончания - 06.06.2023, 17:00:00
#     "TIME_START": "28200",
#     "TIME_FINISH": "61200",
#     "DURATION": "30761",          # Продолжительность
#     "TIME_LEAKS": "2239",         # Предположительно паузы
#     "ACTIVE": false,
#     "PAUSED": false,
#     "CURRENT_STATUS": "CLOSED"
#   },
#   "LAST_PAUSE": {
#     "DATE_START": "1686044626",
#     "DATE_FINISH": "1686046130"
#   },
#   "SOCSERV_ENABLED": true,
#   "SOCSERV_ENABLED_USER": false,
#   "PLANNER": {
#     "TASKS_ENABLED": true,
#     "TASKS": [],
#     "TASKS_COUNT": "0",
#     "TASKS_TIMER": false,
#     "TASK_ON_TIMER": false,
#     "MANDATORY_UFS": "N",
#     "TASK_ADD_URL": "/company/personal/user/1969/tasks/task/edit/0/?ADD_TO_TIMEMAN=Y",
#     "CALENDAR_ENABLED": true,
#     "EVENTS": [],
#     "EVENT_TIME": ""
#   },
#   "FULL": true,
#   "REPORT": "",
#   "REPORT_TS": "1686035883"
# }
