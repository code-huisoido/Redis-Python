#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import uuid

r = redis.Redis(host='localhost', port=6379)

def acquire_lock(conn, lockname, acquire_timeout=10):
    identifier = str(uuid.uuid4())

    end = time.time() + acquire_timeout
    while time.time() < end:
        if conn.setnx('lock:' + lockname, identifier):
            return identifier
        time.sleep(.001)
    return False