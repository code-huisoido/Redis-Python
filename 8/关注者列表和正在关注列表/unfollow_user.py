#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
import redis

HOME_TIMELINE_SIZE = 1000

r = redis.Redis(host='localhost', port=6379)

def unfollow_user(conn, uid, other_uid):
    fkey1 = 'following:%s'%uid
    fkey2 = 'followers:%s'%other_uid

    if not conn.zscore(fkey1, other_uid):
        return None

    pipeline = conn.pipeline(True)
    pipeline.zrem(fkey1, other_uid)
    pipeline.zrem(fkey2, uid)
    pipeline.zrevrange('profile:%s'%other_uid, 0, HOME_TIMELINE_SIZE-1)
    following, followers, statuses = pipeline.execute()[-3:]

    pipeline.hincrby('user:%s'%uid, 'following', -int(following))
    pipeline.hincrby('user:%s'%other_uid, 'followers', -int(followers))
    if statuses:
        pipeline.zrem('home:%s'%uid, *statuses)

    pipeline.execute()
    return True