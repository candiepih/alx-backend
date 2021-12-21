#!/usr/bin/env python3
"""
Basic caching class implementing the BasicCache class.
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Basic caching example.
    """
    def __init__(self):
        """
        Basic caching example.
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        Add an item in the cache.

        Args:
            key (str): The key of the item to add.
            item (str): The item to add.

        Returns:
            None
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            str: The item associated with the given key.
            None: if the key is not in the cache or if the key is None.
        """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
