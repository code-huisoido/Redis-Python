#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
from create_status import create_status
POSTS_PER_PASS = 1000
HOME_TIMELINE_SIZE = 1000

r = redis.Redis()

def post_status(conn, uid, message, **data):
    id = create_status(conn, uid, message, **data)
    if not id:
        return None

    posted = conn.hget('status:%s'%id, 'posted')
    if not posted:
        return None

    post = {str(id): float(posted)}
    conn.zadd('profile:%s'%uid, **post)

    syndicate_status(conn, uid, post)
    return id

def syndicate_status(conn, uid, post, start=0):
    followers = conn.zrangebyscore('followers:%s'%uid, start, 'inf', start=0, num=POSTS_PER_PASS, withscores=True)

    pipeline = conn.pipeline(False)
    for follower, start in followers:
        pipeline.zadd('home:%s'%follower, **post)
        pipeline.zremrangebyrank('home:%s'%follower, 0, -HOME_TIMELINE_SIZE-1)
    pipeline.execute()
    if len(followers) >= POSTS_PER_PASS:
        execute_later(conn, 'default', 'syndicate_status', [conn, uid, post, start])

print post_status(r, 3, "I'm Steven, i like playing basketball!", )