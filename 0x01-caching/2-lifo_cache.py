#!/usr/bin/python3
"""
Implements a LIFO caching system
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Implements a caching class using the LIFO algorithm
    """

    def __init__(self):
        """ Instantiation method
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Puts an item in the cache
            Dicards an item using the LIFO algorithm
        """
        if key and item:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key, _ = self.cache_data.popitem(True)
                    print('DISCARD: {}'.format(first_key))
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=True)

            else:
                self.cache_data[key] = item
                self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        '''
        Gets an item from the cache
        '''
        return self.cache_data.get(key, None)
