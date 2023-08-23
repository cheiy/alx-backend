#!/usr/bin/env python3
"""
Module contains FIFOCache class definition
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        """
        Self initialization
        """
        BaseCaching.__init__(self)

    def put(self, key, item):
        """
        Assigns the value in item to the key called key in the
        self.cache_data dictionary
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                for i in self.cache_data:
                    first_item = i
                    break
                self.cache_data.pop(first_item)
                print("DISCARD: {}".format(first_item))

    def get(self, key):
        """
        Returns the value of key in self.cache_data
        """
        if key is None or self.cache_data.get(key) is None:
            return None
