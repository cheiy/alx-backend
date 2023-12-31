#!/usr/bin/env python3
"""
Module contains the BasicCache class that inherits from BaseCaching
"""
from base_caching import BaseCaching
from typing import Dict


class BasicCache(BaseCaching):
    """
    This class inherits from BaseCaching and is a caching system
    """
    def put(self, key: str, item: str) -> None:
        """
        function assigns the item value to the dictionary cache_data for
        the key called key
        """
        if key is not None and item is not None:
            self.cache_data.update({key: item})

    def get(self, key: str) -> Dict[str, str]:
        """
        Function returns the value in self.cache_data linked to key
        """
        return self.cache_data.get(key)
