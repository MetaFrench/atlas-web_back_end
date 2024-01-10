#!/usr/bin/env python3
"""LRU Caching"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Create the LRUCache class inheriting from BaseCaching"""

    def __init__(self):
        """Initialize the LRUCache class"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        """Update the order if the key already exists"""
        if key in self.cache_data:
            """Update the value for an existing key"""
            self.cache_data[key] = item
            """Remove the existing key from the queue"""
            self.order.remove(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """Discard the least recently used item (LRU)"""
                lru_key = self.order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

        """Add or update the item in the cache"""
        self.cache_data[key] = item
        """Append the new key to the end of the queue"""
        self.order.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        """Update the order as the key was used (most recently)"""
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
