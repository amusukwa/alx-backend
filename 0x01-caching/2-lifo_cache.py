#!/usr/bin/python3
""" LIFOCache module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the LIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the last item added to the cache (LIFO)
                last_key = next(reversed(self.cache_data))
                del self.cache_data[last_key]
                print("DISCARD:", last_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
