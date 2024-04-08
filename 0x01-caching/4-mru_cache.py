#!/usr/bin/python3
"""MRU Cache Replacement Implementation Class
"""
from collections import OrderedDict
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Implements a caching class using the MRU algorithm
    """

    def __init__(self):
        """ Instantiation method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Puts an item in the cache
            Dicards an item using the MRU algorithm
        """

        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    MRU_key, _ = self.cache_data.popitem(False)
                    print('DISCARD:', MRU_key)
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=False)
            else:
                self.cache_data[key] = item

    def get(self, key):
        """ Gets an item from the cache
        """
        if key and key in self.cache_data:
            self.cache_data.move_to_end(key, last=False)
        return self.cache_data.get(key, None)
