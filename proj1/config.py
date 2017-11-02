# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from datetime import timedelta
from kombu import Exchange, Queue

# from kombu.common import Broadcast
# from celery.schedules import crontab

BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/1'

BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 3600}  # 1 hour.
CELERY_IGNORE_RESULT = True

# queue_1与queue_2为消息队列名称
# Exchange:为交换机实例，具有不同的类型。详细参考
# routing_key:用来告知exchange将task message传送至相对应的queue



CELERY_QUEUES = (
    Queue('queue_1', Exchange('Exchange1', type='direct'), routing_key='queue_1_key'),
    Queue('queue_2', Exchange('Exchange2', type='direct'), routing_key='queue_2_key'),
)
CELERY_ROUTES = {
    'proj1.tasks.test_queue_1': {'queue': 'queue_1', 'routing_key': 'queue_1_key'},
    'proj1.tasks.test_queue_2': {'queue': 'queue_2', 'routing_key': 'queue_2_key'},
}

# 广播模式
# CELERY_QUEUES = (
#     Broadcast('broadcast_tasks'),  # 此处设置消息队列broadcast为广播模式，及该队列上的消息会发送至所有监听它的worker
# )
# CELERY_ROUTES = {
#     'proj1.tasks.test_broadcast': {'queue': 'broadcast_tasks'}
# }


CELERY_TIMEZONE = 'Asia/Shanghai'

CELERYBEAT_SCHEDULE = {
    'queue1-every-10-seconds': {
        'task': 'proj1.tasks.test_queue_1',
        'schedule': timedelta(seconds=10),
        'args': ()
    },
    'queue2-every-15-seconds': {
        'task': 'proj1.tasks.test_queue_2',
        'schedule': timedelta(seconds=15),
        'args': ()
    },
}
