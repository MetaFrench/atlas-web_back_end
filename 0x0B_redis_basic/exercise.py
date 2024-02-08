#!/usr/bin/env python3
import redis
import uuid


class Cache:

    def __init__(self):
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        value = self._redis.get(key)
        if fn:
            return fn(value)
        return value

    def get_str(self, key):
        return self.get(key, lambda x: x.decode('utf-8'))

    def get_int(self, key):
        return self.get(key, int)
