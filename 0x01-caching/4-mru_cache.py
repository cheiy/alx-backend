#!/usr/bin/env python3
"""
Module contains MRUCache (Least Recently Used Cache) class definition
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class inherits from BaseCaching and is a caching system implementing
    the Most Recently Used cache policy.
    """

    def __init__(self):
        """
        Self initialization
        """
        BaseCaching.__init__(self)
        self.most_recent = []

    def put(self, key, item):
        """
        Assigns the value in item to the key called key in the
        self.cache_data dictionary
        """
        if key is not None and item is not None:
            if self.cache_data.__contains__(key):
                self.cache_data.update({key: item})
                self.most_recent.append(self.cache_data.get(key))
            else:
                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    discarded_item = self.cache_data.popitem()
                    print("DISCARD: {}".format(discarded_item[0]))
                    self.cache_data.update({key: item})
                elif len(self.cache_data) < BaseCaching.MAX_ITEMS:
                    self.cache_data.update({key: item})
                elif len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    if self.most_recent.__contains__(key) is True:
                        discarded_item = self.cache_data.pop(key)
                        print("DISCARD: {}".format(discarded_item[0]))
                        self.cache_data.update({key: item})

    def get(self, key):
        """
        Returns the value of key in self.cache_data
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            self.most_recent.append(self.cache_data.get(key))
            return self.cache_data.get(key)
