#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

r.rpush('sort-input', 23, 15, 510, 3, 7)
# 根据数字大小对元素进行排序
print r.sort('sort-input')

# 根据字母表顺序(如果是数字，按第一位数字排序)
#r.rpush('sort-input', 'B', 'F', 'D', 'A', 'C')
print r.sort('sort-input', alpha=True)

r.hset('d-7', 'field', 5)
r.hset('d-15', 'field', 1)
r.hset('d-23', 'field', 9)
r.hset('d-510', 'field', 3)
r.hset('d-3', 'field', 2)

# 将散列的域用作权重
print r.sort('sort-input', by='d-*->field')

print r.sort('sort-input', by='d-*->field', get='d-*->field')