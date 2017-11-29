#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import redis

r = redis.Redis(host='localhost', port=6379)

def get_status_message(conn, uid, timeline='home:', page=1, count=10):
    statuses = conn.zrevrange('%s%s'%(timeline, uid), (page-1)*count, page*count-1)

    pipeline = conn.pipeline(True)
    for id in statuses:
        pipeline.hgetall('status:%s'%id)

    return filter(None, pipeline.execute())

print get_status_message(r, 1, )