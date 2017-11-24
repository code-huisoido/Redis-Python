#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

# 模拟数据
contact_list = ["simon", "sindy", "judy", "july", "john", "kobe", "koko", "kim"]

def add_update_contact(conn, user, contact):
    ac_list = 'recent:' + user
    pipeline = conn.pipeline(True)
    pipeline.lrem(ac_list, contact)
    pipeline.lpush(ac_list, contact)
    pipeline.ltrim(ac_list, 0, 99)
    pipeline.execute()

def remove_contact(conn, user, contact):
    conn.lrem('recent:' + user, contact)

for name in contact_list:
    add_update_contact(r, "hui", name)


print r.lrange("recent:hui", 0, -1)