#!/usr/local/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

r.rpush('list', 'item1')
r.rpush('list', 'item2')
r.rpush('list2', 'item3')

# 将item3从list2弹出并推入list左端
print r.brpoplpush('list2', 'list', 1)
print r.brpoplpush('list2', 'list', 1)
print r.lrange('list', 0, -1)

# 将item2从list弹出并推入list2左端
print r.brpoplpush('list', 'list2', 1)

# 按列表顺序，最先遇到的非空列表执行弹出操作
print r.blpop(['list', 'list2'], 1)
print r.blpop(['list', 'list2'], 1)
print r.blpop(['list', 'list2'], 1)
print r.blpop(['list', 'list2'], 1)
