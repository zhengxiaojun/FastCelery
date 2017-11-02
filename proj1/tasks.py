# -*- coding: UTF-8 -*-

from __future__ import absolute_import
from proj1.celery import app
import time


@app.task
def add(x, y):
    return x + y


@app.task
def sendmail(mail):
    print('sending mail to %s...' % mail['to'])
    time.sleep(2.0)
    print('mail sent.')


@app.task
def getdate(tm):
    print 'current time [%s]' % (str(tm['tm']))
    time.sleep(2.0)


# 增加两个task,test_queue_1与test_queue_2
@app.task
def test_queue_1():
    return 'queue1'


@app.task
def test_queue_2():
    return 'queue2'

# 广播
@app.task
def test_broadcast():
    return 'broadcast'
