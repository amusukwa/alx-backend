#!/usr/bin/python3
""" MRUCache module
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ MRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the MRUCache instance
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.remove_most_recently_used()
            self.cache_data[key] = item

    def remove_most_recently_used(self):
        """ Removes the most recently used item from the cache
        """
        if self.cache_data:
            mru_key = next(reversed(self.cache_data))
            del self.cache_data[mru_key]
            print("DISCARD:", mru_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]
        return None
