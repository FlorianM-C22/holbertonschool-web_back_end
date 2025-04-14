#!/usr/bin/python3
""" BasicCache module
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
    This caching system doesn't have a limit
    """

    def put(self, key, item):
        """ Add an item in the cache
        Args:
            key: key to store the item
            item: item to store
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        Args:
            key: key to get the item
        Returns:
            The value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
