#!/usr/bin/python3
""" BasicCache class """

BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """ Defines a BasicCache class that inherits from BaseCaching """

    def put(self, key, item):
        """ Adds an item to the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Retrieves an item from the cache """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
