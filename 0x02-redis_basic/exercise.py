#!/usr/bin/env python3
"""
Module: Redis NoSQL data storage.
"""
import uuid
import redis
from typing import Union


class Cache:
    """
    Represents object for storing data in Redis data storage.
    """


    def __init__(self) -> None:
        """Initializes a Cache instance."""
        self._redis = redis.Redis()
        self._redis.flushdb()


    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores value in Redis data storage, returns the key."""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key
