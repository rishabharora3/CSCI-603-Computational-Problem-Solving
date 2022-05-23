"""
CSCI-603 Chained Hash Tables Lab 7
file: hashmap.py
description: This program is an implementation of a hash map using chaining for handling collisions.
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""
from collections import namedtuple
from typing import Any, Hashable, Iterator, Iterable, Callable

Entry = namedtuple('Entry', ('key', 'value'))  # used for return type in iterable


class LinkedNode:
    """
    Node for chaining
    """
    __slots__ = "key", "value", "link"
    key: Any
    value: Any
    link: 'LinkedNode'

    def __init__(self, key: Any, value: Any, link: 'LinkedNode' = None) -> None:
        """ Create a new node and optionally link it to an existing one.
            param value: the value to be stored in the new node
            param link: the node linked to this one
        """
        self.key = key
        self.value = value
        self.link = link


class HashMap(Iterable):
    __slots__ = 'table', 'size', 'cap', 'max_load', "hash_func"
    table: list[LinkedNode]
    size: int
    cap: int
    max_load: float

    def __init__(self, hash_func: Callable[[Hashable], Any] = None,
                 initial_num_buckets: int = 100, max_load: float = 0.7) -> None:
        """
        Creates an close-addressed hash map of given size and maximum load factor
        :param initial_num_buckets: Initial size (default 100)
        :param max_load: Max load factor (default 0.7)
        """
        if hash_func is not None:
            self.hash_func = hash_func
        else:
            self.hash_func = self.hash_function
        self.cap = initial_num_buckets if initial_num_buckets > 10 else 10
        self.table = [None for _ in range(self.cap)]
        self.size = 0
        self.max_load = max_load

    def add(self, key: Hashable, value: Any) -> None:
        """
        Adds the given (key,value) to the map as a node, if a linked list already exists at the index calculated,
        the node is prepended
        If same key is present the value is updated and returned
        :param key: Key of new entry
        :param value: Value of new entry
        :return: None
        """
        index = self.hash_func(key) % self.cap
        cursor = self.table[index]
        while cursor is not None and cursor.key != key:
            cursor = cursor.link
        if cursor is not None:
            cursor.value = value
            return
        new_node = LinkedNode(key, value, self.table[index])
        self.table[index] = new_node
        self.size += 1
        if self.size / self.cap > self.max_load:
            self.rehash(self.cap * 2)

    def contains(self, key: Hashable):
        """
        Returns True/False whether key is present in map
        :param key: Key to look up
        :return: Whether key is present (boolean)
        """
        index = self.hash_func(key) % self.cap
        cursor = self.table[index]
        while cursor is not None and cursor.key != key:
            cursor = cursor.link
        if cursor is not None:
            return True
        else:
            return False

    def get(self, key: Hashable) -> Any:
        """
        Return the value associated with the given key
        :param key: Key to look up
        :return: Value (or None if key not present)
        """
        index = self.hash_func(key) % self.cap
        cursor = self.table[index]
        while cursor is not None and cursor.key != key:
            cursor = cursor.link
        if cursor is not None:
            return cursor.value
        else:
            return None

    def remove(self, key: Hashable) -> None:
        """
        Remove an item from the table
        :param key: Key of item to remove
        :return: Value of given key
        """
        index = self.hash_func(key) % self.cap
        cursor = self.table[index]
        prev_cursor = None
        while cursor is not None and cursor.key != key:
            prev_cursor = cursor
            cursor = cursor.link
        if cursor is not None and prev_cursor is None:
            self.table[index] = cursor.link
        elif cursor is not None and prev_cursor is not None:
            prev_cursor.link = cursor.link
        else:
            return None
        self.size -= 1
        if self.size / self.cap < 1 - self.max_load and \
                self.cap >= 20:
            self.rehash(self.cap // 2)

    def hash_function(self, key: Hashable) -> int:
        """
        Not using Python's built in hash function here since we want to
        have repeatable testing...
        :param key: Key to store
        :return: Hash value for that key
        """
        # if we want to switch to Python's hash function, uncomment this:
        # return hash(key)
        # otherwise use this:
        return len(key)

    def rehash(self, new_size):
        """
        increasing size in case of add
        downsizing in case of remove
        :param new_size:
        :return:
        """
        if new_size == self.cap:
            return
        hashmap = HashMap(self.hash_func, new_size, self.max_load)
        for key, val in self:
            hashmap.add(key, val)
        self.table = hashmap.table
        self.cap = hashmap.cap

    def imbalance(self) -> float:
        """
        for testing imbalance in the two questions given
        :return: average calculated using the chained nodes divided by not
        None elements counts in table
        """
        i = 0
        count_chain = 0
        count_nodes = 0
        while i < self.cap:
            cursor = self.table[i]
            if cursor is not None:
                count_chain += 1
            while cursor is not None:
                count_nodes += 1
                cursor = cursor.link
            i += 1
        average = (count_nodes / count_chain) - 1
        if average < 0:
            average = 0
        return average

    def __iter__(self) -> Iterator[Entry[Hashable, Any]]:
        """
        iterator for hashmap
        :return:
        """
        i = 0
        while i < self.cap:
            cursor = self.table[i]
            while cursor is not None:
                yield cursor.key, cursor.value
                cursor = cursor.link
            i += 1
