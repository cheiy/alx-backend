#!/usr/bin/env python3
"""
Module contains the BasicCache class that inherits from BaseCaching
"""
from BaseCaching import BaseCaching


class BasicCache(BaseCaching):
    """
    Defines the BasicCache class
    """

    def put(self, key, item):
        """
        function assigns the item value to the dictionary cache_data for
        the key called key
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Function returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
