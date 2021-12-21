#!/usr/bin/env python3
"""
Contains LIFOCache that implements LIFO Cache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.lifo_list = []

    def put(self, key, item):
        """
        Put item in cache

        Args:
            key: key to search
            item: item to add

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item
            self.lifo_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                second_last_key = len(self.lifo_list) - 2
                last_key = self.lifo_list.pop(second_last_key)
                del self.cache_data[last_key]
                print("DISCARD: " + last_key)

    def get(self, key):
        """
        Get item from cache

        Args:
            key: key to search

        Returns:
            item if key exists, None otherwise
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
