"""
CSCI-603 Autocomplete Lab 5
file: bsearch.py
description: This program searches a word based on given prefix
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""


def binary_search(sorted_data, value, left, right):
    """
    This method uses binary search to return the index of first instance
    of the word with the prefix passed.
    :param  sorted_data:   sorted list
    :param  value: prefix to be searched
    :param  left:   left index of list
    :param  right:  right index of list
    :return index:
    """
    if left > right:
        return -1
    midindex = (right - left) // 2 + left
    if sorted_data[midindex][0:len(value)] == value:
        indexval = 0 + midindex
        if indexval > indexval + binary_search(sorted_data, value, left, midindex - 1):
            return indexval
        return binary_search(sorted_data, value, left, midindex - 1)
    elif sorted_data[midindex][0:len(value)] > value:
        return binary_search(sorted_data, value, left, midindex - 1)
    else:
        return binary_search(sorted_data, value, midindex + 1, right)
