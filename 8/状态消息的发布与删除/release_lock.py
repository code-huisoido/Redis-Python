#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis

def release_lock(conn, lockname, identifier):
    pipe = conn.pipeline(True)
    lockname = 'lock:' + lockname

    while True:
        try:
            pipe.watch(lockname)
            if pipe.get(lockname) == identifier:
                pipe.multi()
                pipe.delete(lockname)
                pipe.execute()
                return True
                
            pipe.unwatch()
            break

        except redis.exceptions.WatchError:
            pass
    return False