    (celery-env) jack_zheng@mac ~/PycharmProjects/mycelery$python
    Python 2.7.10 (default, Oct 23 2015, 19:19:21)
    [GCC 4.2.1 Compatible Apple LLVM 7.0.0 (clang-700.0.59.5)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>> from proj1.tasks import test_queue_1
    >>> test_queue_1.delay()
    <AsyncResult: fe546db3-a7a0-499e-9a37-adf5f6db1595>
    >>> from proj1.tasks import test_queue_2
    >>> test_queue_2.delay()
    <AsyncResult: 0864c3f7-8787-48c9-87b2-7241e780b664>


    #### 脚本命令  
    celery -A proj1 worker -B --loglevel=info
    #### web监控命令   
    celery flower --port=5555 --broker=redis://127.0.0.1:6379/0
    #### 队列命令,优先级别
    celery -A proj1 worker -Q queue_1 --loglevel=info
    celery -A proj1 worker -Q queue_2 --loglevel=info
