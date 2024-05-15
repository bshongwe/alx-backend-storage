#!/usr/bin/env python3
"""
Module: Redis NoSQL data storage.
"""
import uuid
import redis
from typing import Union, Callable, Any
from functools import wraps


def call_history(func):
    """Tracks call details of Cache class method."""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Returns method output after storing its inputs and output."""
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return invoker


def count_calls(func):
    """Tracks number of calls made to Cache class method."""
    @wraps(method)
    def invoker(self, *args, **kwargs) -> Any:
        """Invokes given method after incrementing its call counter."""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return invoker


class Cache:
    """Represents object for storing data in Redis data storage."""

    def __init__(self) -> None:
        """Initializes a Cache instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores value in Redis data storage, returns the key."""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key

    def get(self, key: str, fn: Callable[[bytes], Any] = None) -> Any:
        """
        Retrieves value from Redis data storage,
        optionally converts it using fn.
        """
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value
        return fn(value)

    def get_str(self, key: str) -> Any:
        """Retrieves a string value from Redis data storage."""
        return self.get(key, lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Any:
        """Retrieves an integer value from Redis data storage."""
        return self.get(key, lambda d: int(d))


if __name__ == "__main__":
    cache = Cache()

    TEST_CASES = {
        b"foo": None,
        123: int,
        "bar": lambda d: d.decode("utf-8")
    }

    for value, fn in TEST_CASES.items():
        key = cache.store(value)
        assert cache.get(key, fn=fn) == value

