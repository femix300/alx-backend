#!/usr/bin/python3
"""Implements a Basic Caching class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic cache class without a standard caching algorithm
    """

    def put(self, key, item):
        """ Puts an Item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return self.cache_data.get(key, None)
