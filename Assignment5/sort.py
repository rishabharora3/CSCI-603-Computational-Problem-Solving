"""
CSCI-603 Autocomplete Lab 5
file: mergesort.py
description: This program searches a word based on given prefix
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""


def merge_sort(unsorted):
    """
    This method uses merge sort technique to sort the unsorted list
    :param unsorted:
    :return sorted list:
    """
    if len(unsorted) == 1:
        return unsorted
    midindex = len(unsorted) // 2
    first = merge_sort(unsorted[0:midindex])
    second = merge_sort(unsorted[midindex:len(unsorted)])
    ans = []
    firstind = 0
    secondind = 0
    while firstind < len(first) and secondind < len(second):
        if first[firstind] < second[secondind]:
            ans.append(first[firstind])
            firstind += 1
        else:
            ans.append(second[secondind])
            secondind += 1

    if firstind < len(first):
        ans.extend(first[firstind:])
    else:
        ans.extend(second[secondind:])
    return ans
