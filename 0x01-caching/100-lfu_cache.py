#!/usr/bin/env python3
"""
LFU Cache
"""

from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    Most Recently Used (MRU) caching system implementation.
    """
    def __init__(self):
        """
        Initialize an LRUCache instance
        """
        super().__init__()
        self.cache_order = []

    def put(self, key, item):
        """
        Get an item by using its key and return it. If the key is not in the
        cache, add it. If the key is in the cache, remove it and add it again.

        Args:
            key: The key of the item to get.
            item: The item to add to the cache.

        Returns:
            The item if it is in the cache, None otherwise.
        """
        if key and item:
            self.cache_data[key] = item
            if key not in self.cache_order:
                self.cache_order.append(key)
            else:
                self.cache_order.remove(key)
                self.cache_order.append(key)
            if len(self.cache_order) > BaseCaching.MAX_ITEMS:
                popped = self.cache_order.pop(0)
                del self.cache_data[popped]
                print("DISCARD: {}".format(str(popped)))

    def get(self, key):
        """
        Get an item by using its key and return it. If the key is not
        in the cache, return None.

        Args:
            key: The key of the item to get.
        """
        if key in self.cache_data:
            self.cache_order.remove(key)
            self.cache_order.append(key)
            return self.cache_data[key]
        return None
