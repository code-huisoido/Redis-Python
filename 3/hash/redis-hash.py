#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis()
print r.hmset('hash-key', {'k1':'v1', 'k2':'v2', 'k3':'v3'})
print r.hmget('hash-key', {'k2', 'k3'})
print r.hlen('hash-key')
print r.hdel('hash-key', 'k1', 'k3')