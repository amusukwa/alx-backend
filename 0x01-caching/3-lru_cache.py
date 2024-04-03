#!/usr/bin/python3
""" LRUCache module
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the LRUCache instance
        """
        super().__init__()
        self.recently_used = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.remove_least_recently_used()
            self.cache_data[key] = item
            self.recently_used.append(key)

    def remove_least_recently_used(self):
        """ Removes the least recently used item from the cache
        """
        if self.recently_used:
            lru_key = self.recently_used.pop(0)
            del self.cache_data[lru_key]
            print("DISCARD:", lru_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.recently_used.remove(key)
            self.recently_used.append(key)
            return self.cache_data[key]
        return None
