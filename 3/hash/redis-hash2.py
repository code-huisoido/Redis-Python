#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis()
r.hmset('hash-key2', {'short':'hello', 'long':1000*'1'})

# 获取所有键
print r.hkeys('hash-key2')

# 获取所有值
print r.hvals('hash-key2')

# 获取单个键值
print r.hget('hash-key2', 'short')

# 获取所有键值
print r.hgetall('hash-key2')

# 判断是否存在某个键值，如果执行增加操作则当初始0处理
print r.hexists('hash-key2', 'num')
print r.hincrby('hash-key2', 'num')
print r.hexists('hash-key2', 'num')