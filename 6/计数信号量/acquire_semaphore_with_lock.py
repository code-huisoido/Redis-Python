#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
from acquire_lock import acquire_lock
from acquire_fair_semaphore import acquire_fair_semaphore
from release_lock import release_lock

r = redis.Redis(host='localhost', port=6379)

def acquire_semaphore_with_lock(conn, semname, limit, timeout=10):
    identifier = acquire_lock(conn, semname, acquire_timeout=.01)
    if identifier:
        try:
            return acquire_fair_semaphore(conn, semname, limit, timeout)
        finally:
            release_lock(conn, semname, identifier)


print acquire_semaphore_with_lock(r, "semaphore:remote", 5)