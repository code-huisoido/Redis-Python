#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host="localhost", port=6379)
print r.get('key')

r.incr('key')
print r.get('key')

r.incr('key', 15)
print r.get('key')

r.decr('key', 5)
print r.get('key')

# 这里字符串2能解析成数字2
r.set('key', '2')
print r.get('key')