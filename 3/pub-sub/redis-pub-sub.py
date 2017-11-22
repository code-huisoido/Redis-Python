#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import threading
import time

r = redis.Redis(host='localhost', port=6379)

def publisher(n):
    time.sleep(1)
    for i in xrange(n):
        r.publish('channel', i)
        time.sleep(1)

def run_pubsub():
    threading.Thread(target=publisher, args=(3,)).start()
    pubsub = r.pubsub()
    pubsub.subscribe(['channel'])
    count = 0
    for item in pubsub.listen():
        print item
        count += 1
        if count == 4:
            pubsub.unsubscribe()
        if count == 5:
            break

run_pubsub()