#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import redis

HOME_TIMELINE_SIZE = 1000

r = redis.Redis(host='localhost', port=6379)

def follow_user(conn, uid, other_uid):
    fkey1 = 'following:%s'%uid
    fkey2 = 'followers:%s'%other_uid

    if conn.zscore(fkey1, other_uid):
        return None

    now = time.time()

    pipeline = conn.pipeline(True)
    pipeline.zadd(fkey1, other_uid, now)
    pipeline.zadd(fkey2, uid, now)
    pipeline.zrevrange('profile:%s'%other_uid, 0, HOME_TIMELINE_SIZE-1, withscores=True)
    following, followers, status_and_score = pipeline.execute()[-3:]

    pipeline.hincrby('user:%s'%uid, 'following', int(following))
    pipeline.hincrby('user:%s'%other_uid, 'followers', int(followers))
    if status_and_score:
        pipeline.zadd('home:%s'%uid, **dict(status_and_score))
    pipeline.zremrangebyrank('home:%s'%uid, 0, -HOME_TIMELINE_SIZE-1)
    
    pipeline.execute()
    return True

print follow_user(r, 3, 3)