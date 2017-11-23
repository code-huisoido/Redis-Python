#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import time
import threading

r = redis.Redis(host='localhost', port=6379)

def trans():
    pipeline = r.pipeline()
    pipeline.incr('trans:', 2)
    time.sleep(.1)
    pipeline.incr('trans:', -1)
    # 返回每条redis命令的执行结果
    print pipeline.execute()

if 1:
    for i in xrange(3):
        threading.Thread(target=trans).start()
    time.sleep(.5)