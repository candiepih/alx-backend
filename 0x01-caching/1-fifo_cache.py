#!/usr/bin/env python3
"""
Contains implementation of a FIFO Cache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache
    """
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.cache_list = []

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
            self.cache_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                self.cache_data.pop(self.cache_list[0])
                popped = self.cache_list.pop(0)
                print("DISCARD: {}".format(popped))

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
