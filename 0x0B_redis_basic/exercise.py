#!/usr/bin/env python3
"""
Redis Cache Module
"""

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Decorator that counts method calls using Redis
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def replay(method: Callable):
    """
    Display the history of calls of a particular function
    """
    # Create a Redis instance to access the stored data
    r = redis.Redis()
    key = method.__qualname__
    inputs = f"{key}:inputs"
    outputs = f"{key}:outputs"
    count = r.get(key)
    inputs_list = r.lrange(inputs, 0, -1)
    outputs_list = r.lrange(outputs, 0, -1)

    print(f"{key} was called {count.decode('utf-8') if count else 0} times:")
    for i, o in zip(inputs_list, outputs_list):
        print(f"{key}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


def call_history(method: Callable) -> Callable:
    """
    Decorator that stores method calls in Redis
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        key = method.__qualname__
        inputs = f"{key}:inputs"
        outputs = f"{key}:outputs"
        self._redis.rpush(inputs, str(args))
        data = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(data))
        return data
    return wrapper


class Cache:
    def __init__(self):
        """
        Initialize the Redis connection
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the data in the cache
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[str, bytes,
                                                          int, float]:
        """
        Get the data from the cache
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> str:
        """
        Get the data from the cache as a string
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
        Get the data from the cache as an integer
        """
        return self.get(key, int)
