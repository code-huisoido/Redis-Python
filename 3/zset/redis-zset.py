#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

# python客户端与redis的先score后member操作相反
print r.zadd('zset-key', 'a', 3, 'b', 2, 'c', 1)

# 取得集合大小
print r.zcard('zset-key')

# 自增分数
print r.zincrby('zset-key', 'c', 3)

# 获取某个成员分数
print r.zscore('zset-key', 'b')

# 获取指定成员的排名，从0开始算
print r.zrank('zset-key', 'c')

# 统计给定分数范围内的元素数量
print r.zcount('zset-key', 0, 3)

# 删除成员
print r.zrem('zset-key', 'b')

# 取出范围内的成员
print r.zrange('zset-key', 0, -1, withscores=True)


