#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import time
import uuid

r = redis.Redis(host='localhost', port=6379)

def acquire_semaphore(conn, semname, limit, timeout=10):
    identifier = str(uuid.uuid4())
    now = time.time()

    pipeline = conn.pipeline(True)

    pipeline.zremrangebyscore(semname, '-inf', now - timeout)
    pipeline.zadd(semname, identifier, now)
    pipeline.zrank(semname, identifier)
    if pipeline.execute()[-1] < limit:
        return identifier
    
    conn.zrem(semname, identifier)
    return None

for num in range(0, 5):
    print acquire_semaphore(r, "semaphore:remote", 5)