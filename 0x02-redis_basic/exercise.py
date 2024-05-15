#!/usr/bin/env python3
"""
Module: Redis NoSQL data storage.
"""
import uuid
import redis
from typing import Union


def call_history(func):
    def wrapper(*args, **kwargs):
        # Placeholder for actual call history logic
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

def count_calls(func):
    def wrapper(*args, **kwargs):
        # Placeholder for actual count calls logic
        print(f"Counting call to {func.__name__}")
        return func(*args, **kwargs)
    return wrapper


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


if __name__ == "__main__":
    cache = Cache()
    key = cache.store("Hello, Redis!")
    print(f"Stored data with key: {key}")

