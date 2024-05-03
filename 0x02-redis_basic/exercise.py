#!/usr/bin/env python3
"""
start up
"""
import random
from typing import Callable, Union
import redis
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    @wraps(method)
    def wrapper(self, *args, **kwds):
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


class Cache:
    def __init__(self):
        """
        init method
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        store method
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> Union[bytes, None]:
        """
        get method
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> Union[str, None]:
        """
        retrieves data from Redis and converts it to a string.
        """
        return self.get(key, fn=str)

    def get_int(self, key: str) -> Union[int, None]:
        """
        retrieves data from Redis and converts it to a int.
        """
        return self.get(key, fn=int)
