#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)
r.sadd('skey1', 'a', 'b', 'c', 'd')
r.sadd('skey2', 'c', 'd', 'e', 'f')

print r.sdiff('skey1', 'skey2')
print r.sinter('skey1', 'skey2')
print r.sunion('skey1', 'skey2')