#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

r.zadd('zset-1', 'a', 1, 'b', 2, 'c', 3)
r.zadd('zset-2', 'b', 4, 'c', 1, 'd', 0)

# 交集，默认合并成员分值，有sum、min、max三种模式
r.zinterstore('zset-i', ['zset-1', 'zset-2'])
print r.zrange('zset-i', 0, -1, withscores=True)

# 并集
print r.zunionstore('zset-u', ['zset-1', 'zset-2'], aggregate='min')
print r.zrange('zset-u', 0, -1, withscores=True)

# 可以把集合和有序集合合并，集合的成员分值默认全为1
print r.sadd('set-1', 'a', 'd')
print r.zunionstore('zset-u2', ['zset-1', 'zset-2', 'set-1'])
print r.zrange('zset-u2', 0, -1, withscores=True)