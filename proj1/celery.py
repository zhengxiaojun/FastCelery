# -*- coding:utf-8 -*-

from __future__ import absolute_import  # 定义未来文件的绝对进口，而且绝对进口必须在每个模块的顶部启用。
from celery import Celery  # 从celery导入Celery的应用程序接口

app = Celery('proj1', include=['proj1.tasks'])

app.config_from_object('proj1.config')

if __name__ == '__main__':
    app.start()
