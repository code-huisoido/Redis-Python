#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
import uuid
import time
import acquire_lock
from acquire_lock import acquire_lock
import release_lock
from release_lock import release_lock

r = redis.Redis()

def purchase_item_with_lock(conn, buyerid, itemid, sellerid):
    buyer = "users:%s"%buyerid
    seller = "users:%s"%sellerid
    item = "%s.%s"%(itemid, sellerid)
    inventory = "inventory:%s"%buyerid
    # 这里有两种选择，第一种是锁住整个market，第二种只锁住某个商品
    #market = "market:"
    market = "market:%s"%item

    locked = acquire_lock(conn, market)
    if not locked:
        return False

    pipe = conn.pipeline(True)
    try:
        pipe.zscore("market:", item)
        pipe.hget(buyer, 'funds')
        price, funds = pipe.execute()
        if price is None or price > funds:
            return None

        pipe.hincrby(seller, 'funds', int(price))
        pipe.hincrby(buyer, 'funds', int(-price))
        pipe.sadd(inventory, itemid)
        pipe.zrem("market:", item)
        pipe.execute()
        return True
    finally:
        release_lock(conn, market, locked)

print purchase_item_with_lock(r, 27, "itemM", 17)        