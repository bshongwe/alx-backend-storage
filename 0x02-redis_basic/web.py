#!/usr/bin/env python3
"""
Module: Request caching and tracking tools
"""
import requests
import redis
from functools import wraps
from typing import Callable

"""
Redis instance
"""
redis_instance = redis.Redis()


def track_and_cache(method: Callable) -> Callable:
    """Decorator to track and cache the results of a function."""

    @wraps(method)
    def wrapper(url: str) -> str:
        """
        Wrapper function to track and cache results.
        access_count_key: tracking access count
        cache_key: cache result key
        """
        access_count_key = f"count:{url}"
        cache_key = f"cache:{url}"

        redis_instance.incr(access_count_key)

        cached_result = redis_instance.get(cache_key)
        if cached_result:
            return cached_result.decode('utf-8')

        result = method(url)

        redis_instance.setex(cache_key, 10, result)

        return result

    return wrapper


@track_and_cache
def get_page(url: str) -> str:
    """Function to obtain the HTML content of a URL."""
    response = requests.get(url)
    return response.text


if __name__ == "__main__":
    """
    Test the get_page function
    """
    url = "http://slowwly.robertomurray.co.uk"
    print(get_page(url))
    print(get_page(url))

# 1st call delay, creates cache
# 2nd call, brings back cache
