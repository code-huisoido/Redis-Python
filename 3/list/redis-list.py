#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

# 推入队列
r.rpush('list-key', 'last')
r.lpush('list-key', 'first')
r.rpush('list-key', 'new last')

# 显示范围内的队列元素
print r.lrange('list-key', 0, -1)

# 弹出队列
print r.lpop('list-key')
print r.lpop('list-key')

print r.lrange('list-key', 0, -1)

# 多个元素推入队列
r.rpush('list-key', 'a', 'b', 'c')
print r.lrange('list-key', 0, -1)

# 对列表进行修剪
r.ltrim('list-key', 2, -1)
print r.lrange('list-key', 0, -1)
