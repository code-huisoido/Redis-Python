#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

# 集合添加与删除
print r.sadd('set-key', 'a', 'b', 'c')
print r.srem('set-key', 'c', 'd')
print r.srem('set-key', 'c', 'd')

# 返回集合包含的元素数量
print r.scard('set-key')

# 返回集合包含的元素
print r.smembers('set-key')

# 移动元素到另一个集合
print r.smove('set-key', 'set-key2', 'a')
print r.smove('set-key', 'set-key2', 'c')
print r.smembers('set-key2')

