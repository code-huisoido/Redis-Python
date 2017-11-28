#!/usr/bin/python
# -*- coding:utf-8 -*-
import time
from release_fair_semaphore import release_fair_semaphore

def refresh_fair_semaphore(conn, semname, identifier):
    if conn.zadd(semname, identifier, time.time()):
        release_fair_semaphore(conn, semname, identifier)
        return False
    return True