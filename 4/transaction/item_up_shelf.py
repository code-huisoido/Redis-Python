#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import time

r = redis.Redis()
# 模拟数据
r.hmset('users:17', {'name':'Frank', 'funds':43})
r.hmset('users:27', {'name':'Bill', 'funds':125})
r.sadd('inventory:17', 'itemL', 'itemM', 'itemN')
r.sadd('inventory:27', 'itemO', 'itemP', 'itemQ')

def list_item(conn, itemid, sellerid, price):
    inventory = "inventory:%s"%sellerid
    item = "%s.%s"%(itemid, sellerid)
    end = time.time() + 5
    pipe = conn.pipeline()

    while time.time() < end:
        try:
            pipe.watch(inventory)
            if not pipe.sismember(inventory, itemid):
                pipe.unwatch()
                return None
            
            pipe.multi()
            pipe.zadd("market:", item, price)
            pipe.srem(inventory, itemid)
            pipe.execute()
            return True
        except redis.exceptions.WatchError:
            pass
    return False

# 执行商品上架操作
print list_item(r, "itemM", 17, 97)