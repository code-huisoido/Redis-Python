#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
from acquire_lock_with_timeout import acquire_lock_with_timeout
from release_lock import release_lock

FOLLOWERS_LIMIT = 1000
HOME_TIMELINE_SIZE = 1000

r= redis.Redis()

def delete_status(conn, uid, status_id):
    key = 'status:%s'%status_id
    lock = acquire_lock_with_timeout(conn, key, 1)
    if not lock:
        return None

    if conn.hget(key, 'uid') != str(uid):
        release_lock(conn, key, lock)
        return None

    pipeline = conn.pipeline(True)
    pipeline.delete(key)
    pipeline.zrem('profile:%s'%uid, status_id)
    # 书中这个代码感觉是没必要的，发布消息时是没有往自己的home时间线插入
    pipeline.zrem('home:%s'%uid, status_id)
    # 书中练习题目
    delete_homeline_status(r, uid, status_id)
    pipeline.hincrby('user:%s'%uid, 'posts', -1)
    pipeline.execute()

    release_lock(conn, key, lock)
    return True

def delete_homeline_status(conn, uid, status_id, start=0):
    # inf是无穷大的意思，-inf代表无穷小
    followers = conn.zrangebyscore('followers:%s'%uid, start, 'inf', start=0, num=FOLLOWERS_LIMIT, withscores=True)
    
    pipeline = conn.pipeline(False)
    for follower,start in followers:
        pipeline.zrem('home:%s'%follower, status_id)
    pipeline.execute()
    if len(followers) > HOME_TIMELINE_SIZE:
        execute_later(conn, 'default', 'delete_homeline_status', [conn, uid, status_id, start])

print delete_status(r, 2, 3)