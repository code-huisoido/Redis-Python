#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import time
import threading

r = redis.Redis(host='localhost', port=6379)

def notrans():
    print r.incr('notrans:')
    time.sleep(.1)
    r.incr('notrans:', -1)

# 书上可能是为了美观才加if 1
if 1:
    for i in xrange(3):
        threading.Thread(target=notrans).start()
    time.sleep(.5)