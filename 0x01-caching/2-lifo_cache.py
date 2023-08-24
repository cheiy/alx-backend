#!/usr/bin/env python3
"""
Module contains LIFOCache class definition
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
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
            if self.cache_data.__contains__(key):
                self.cache_data.update({key: item})
            else:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    discarded_item = self.cache_data.popitem()
                    print("DISCARD: {}".format(discarded_item[0]))
                    self.cache_data.update({key: item})
                elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
                    self.cache_data.update({key: item})
                elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    discarded_item = self.cache_data.popitem()
                    print("DISCARD: {}".format(discarded_item[0]))
                    self.cache_data.update({key: item})

    def get(self, key):
        """
        Returns the value of key in self.cache_data
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
