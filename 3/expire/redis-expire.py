#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import time

r = redis.Redis(host='localhost', port=6379)

r.set('key', 'value')
print r.get('key')
r.expire('key', 2)

time.sleep(2)
print "2秒过后，".decode("utf-8"), r.get('key')

r.set('key', 'value2')
r.expire('key', 100)
print r.ttl('key')
