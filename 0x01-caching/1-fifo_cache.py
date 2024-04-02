#!/usr/bin/python3
""" FIFOCache module
"""
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the FIFOCache instance
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                # Remove the first item added to the cache
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print("DISCARD:", first_key)
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
