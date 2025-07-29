#!/usr/bin/env python3
"""
Redis Cache Module
"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self):
        """
        Initialize the Redis connection
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in the cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
