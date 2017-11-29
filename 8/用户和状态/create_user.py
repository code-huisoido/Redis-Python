#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import time
from release_lock import release_lock
from acquire_lock_with_timeout import acquire_lock_with_timeout

r = redis.Redis(host='localhost', port=6379)

def create_user(conn, login, name):
    llogin = login.lower()
    lock = acquire_lock_with_timeout(conn, 'user:' + llogin, 1)
    if not lock:
        return None

    if conn.hget('users:', llogin):
        release_lock(conn, 'user:' + llogin, lock)
        return None

    id = conn.incr('user:id:')
    pipeline = conn.pipeline(True)
    pipeline.hset('users:', llogin, id)
    pipeline.hmset('user:%s'%id, {
        'login': login,
        'id': id,
        'name': name,
        'followers': 0,
        'following': 0,
        'posts': 0,
        'signup': time.time(),
    })

    pipeline.execute()
    release_lock(conn, 'user:' + llogin, lock)
    return id

print create_user(r, "jack", "hui")