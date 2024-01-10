#!/usr/bin/env python3
"""MRU Caching"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """Create the MRUCache class inheriting from BaseCaching"""

    def __init__(self):
        """Initialize the MRUCache class"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache"""
        if key is None or item is None:
            return

        """Update the order if the key already exists"""
        if key in self.cache_data:
            """Update the value for an existing key"""
            self.cache_data[key] = item
            """Remove the existing key from the queue"""
            self.queue.remove(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """ Discard the most recently used item (MRU)"""
                mru_key = self.queue.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

        """Add or update the item in the cache"""
        self.cache_data[key] = item
        self.queue.append(key)

    def get(self, key):
        """Retrieve an item from the cache"""
        if key is None or key not in self.cache_data:
            return None

        """Update the order of the key as MRU"""
        self.queue.remove(key)
        self.queue.append(key)

        return self.cache_data[key]
