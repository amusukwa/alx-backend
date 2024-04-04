#!/usr/bin/python3
""" LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ LFUCache inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """ Initializes the LFUCache instance
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                self.remove_least_frequency_used()
            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def remove_least_frequency_used(self):
        """ Removes the least frequency used item from the cache
        """
        min_frequency = min(self.frequency.values())
        least_frequent_keys = [key for key, freq in self.frequency.items() if freq == min_frequency]

        if len(least_frequent_keys) == 1:
            lfu_key = least_frequent_keys[0]
        else:
            lfu_key = min(self.cache_data, key=lambda x: self.cache_data[x])

        del self.cache_data[lfu_key]
        del self.frequency[lfu_key]
        print("DISCARD:", lfu_key)

    def get(self, key):
        """ Get an item by key
        """
        if key is not None and key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
