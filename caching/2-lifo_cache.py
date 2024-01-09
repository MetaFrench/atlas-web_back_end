#!/usr/bin/env python3
"""Last-In-First-Out (LIFO) Caching"""

from BaseCaching import BaseCaching
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """Class implementing LIFO caching strategy"""

    def __init__(self):
        """Initializes the LIFO cache"""
        super().__init__()
        self.queue = []  # List to maintain the order of keys

    def put(self, key, item):
        """Adds or updates an item in the cache"""
        if key is None or item is None:
            return

        if key in self.cache_data:
            """Update the value for an existing key"""
            self.cache_data[key] = item
            """Remove the existing key from the queue"""
            self.queue.remove(key)
        else:
            if len(self.cache_data) >= self.MAX_ITEMS:
                """LIFO: Remove the last item added to the cache"""
                last_key = list(self.cache_data.keys())[-1]
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

        """Add or update the item in the cache"""
        self.cache_data[key] = item
        """Append the new key to the end of the queue"""
        self.queue.append(key)

    def get(self, key):
        """Retrieves the value associated with the given key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
