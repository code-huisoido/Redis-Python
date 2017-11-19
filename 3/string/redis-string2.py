#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)
r.append('new-string-key', 'hello ')
r.append('new-string-key', 'world!')
print r.get('new-string-key')

# 截取字符串
print r.substr('new-string-key', 3, 7)

# 替换字符串
r.setrange('new-string-key', 0, 'H')
r.setrange('new-string-key', 6, 'W')
print r.get('new-string-key')

# 扩展字符串
r.setrange('new-string-key', 11, ', how are you?')
print r.get('new-string-key')

# 设置二进制位串 00100001 => 33
r.setbit('another-key', 2, 1)
r.setbit('another-key', 7, 1)
print r.getbit('another-key', 6)
print r.get('another-key')
