#!/usr/bin/env python3
"""
Least Recently Used (LRU) cache implementation
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Least Recently Used (LRU) cache implementation
    """

    def __init__(self):
        """
        Initialize an LRUCache instance
        """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """
        Add an item in the cache

        If the key already exists, update the value of the
        key and move the key to the end of the cache list.

        If the cache is full, remove the oldest item from
        the cache, and add the new item in the cache.

        Args:
            key: The key of the item to be added
            item: The item to be added

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_list:
                self.cache_list.append(key)
            else:
                self.cache_list.remove(key)
                self.cache_list.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = self.cache_list.pop(0)
                del self.cache_data[popped]
                print("DISCARD: {}".format(popped))

    def get(self, key):
        """
        Get an item by using its key and return it.
        Remove the item from the cache_list and add it
        to the end of the cache_list.

        Args:
            key: The key of the item to be returned

        Returns:
            The value of the item
        """
        if key:
            if key in self.cache_data:
                self.cache_list.remove(key)
                self.cache_list.append(key)
                return self.cache_data[key]
        return None
