#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import bisect
r = redis.Redis(host='localhost', port=6379)

valid_characters = '`abcdefghijklmnopqrstuvwxyz{'

def find_prefix_range(prefix):
    posn = bisect.bisect_left(valid_characters, prefix[-1:])
    suffix = valid_characters[(posn or 1) - 1]
    return prefix[:-1] + suffix + '{', prefix + '{'

print find_prefix_range("ko")