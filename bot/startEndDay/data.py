import fake_useragent


user = fake_useragent.UserAgent().random
headers = {
    'User-Agent': user,
}



""" Пример ещё не открытого дня на 27.06.2023 """
# {
#     'ID': '53433',
#     'STATE': 'CLOSED',   !!!
#     'CAN_EDIT': 'N',  !!!
#     'CAN_OPEN': 'OPEN',
#     'REPORT_REQ': 'A',
#     'TM_FREE': False,
#     'INFO': {
#         'DATE_START': '1687761868', # 26.06.2023 - Предыдущий день
#         'DATE_FINISH': '1687793192',
#         'TIME_START': '35068', # 9 hours, 44 min 28 sec.
#         'TIME_FINISH': '66392', # 18 hours, 26 min 32 sec.
#         'DURATION': '31324', # 8 hours, 42 min 4 sec.
#         'TIME_LEAKS': '0',
#         'ACTIVE': T rue,
#         'PAUSED': False,
#         'CURRENT_STATUS': 'CLOSED'
#     },
#     'SOCSERV_ENABLED': True,
#     'SOCSERV_ENABLED_USER': False,
#     'PLANNER': {
#         'TASKS_ENABLED': True,
#         'TASKS': [],
#         'TASKS_COUNT': '0',
#         'TASKS_TIMER': False,
#         'TASK_ON_TIMER': False,
#         'MANDATORY_UFS': 'N',
#         'TASK_ADD_URL': '/company/personal/user/1969/tasks/task/edit/0/?ADD_TO_TIMEMAN=Y',
#         'CALENDAR_ENABLED': True,
#         'EVENTS': [],
#         'EVENT_TIME': ''
#     },
#     'FULL': True,
#     'REPORT': '',
#     'REPORT_TS': '1687761868'
# }

""" Пример открытого дня на 27.06.2023 """
# {
#     'ID': '53559',
#     'STATE': 'OPENED',
#     'CAN_EDIT': 'Y',  !!!
#     'REPORT_REQ': 'A',
#     'TM_FREE': False,
#     'INFO': {
#         'DATE_START': '1687852065', # Tue, 27 Jun 2023 07:47:45 GMT
#         'DATE_FINISH': '',
#         'TIME_START': '38865', # 10 hours, 47 min 45 sec.
#         'TIME_FINISH': '',
#         'DURATION': '405',
#         'TIME_LEAKS': '0',
#         'ACTIVE': True,
#         'PAUSED': False,
#         'CURRENT_STATUS': 'OPENED',
#         'RECOMMENDED_CLOSE_TIMESTAMP': '1687878000'
#     },
#     'SOCSERV_ENABLED': True,
#     'SOCSERV_ENABLED_USER': False,
#     'PLANNER': {
#         'TASKS_ENABLED': True,
#         'TASKS': [],
#         'TASKS_COUNT': '0',
#         'TASKS_TIMER': False,
#         'TASK_ON_TIMER': False,
#         'MANDATORY_UFS': 'N',
#         'TASK_ADD_URL': '/company/personal/user/1969/tasks/task/edit/0/?ADD_TO_TIMEMAN=Y',
#         'CALENDAR_ENABLED': True,
#         'EVENTS': [],
#         'EVENT_TIME': ''
#     },
#     'FULL': True,
#     'REPORT': '',
#     'REPORT_TS': '1687852065'
# }
