# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from datetime import timedelta
from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULE = {
    'add-every-5-seconds': {
        'task': 'proj1.tasks.add',
        'schedule': timedelta(seconds=5),
        'args': (16, 16)
    },
}

# crontab

# CELERYBEAT_SCHEDULE = {
#     # Executes every Monday morning at 7:30 A.M
#     'add-every-monday-morning': {
#         'task': 'proj1.tasks.add',
#         'schedule': crontab(hour=19, minute=22, day_of_week=3),
#         'args': (16, 16),
#     },
# }


# 脚本命令  celery -A proj1 worker -B --loglevel=info

# web监控命令   celery flower --port=5555 --broker=redis://127.0.0.1:6379/0