#!/usr/bin/python
# -*- coding:utf-8 -*-
import redis
r = redis.Redis(host='localhost', port=6379)

def fetch_autocomplete_list(conn, user, prefix):
    candidates = conn.lrange("recent:" + user, 0, -1)
    matches = []
    for candidate in candidates:
        if candidate.lower().startswith(prefix):
            matches.append(candidate)
    return matches

# 返回匹配结果
print fetch_autocomplete_list(r, "hui", "j")