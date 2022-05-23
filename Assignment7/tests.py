"""
file: tests.py
description: Verify the chained hash map class implementation
"""

__author__ = ["ka7982 Karan Ahluwalia", "ra8851 Rishabh Arora"]

from hashmap import HashMap


# from word_count import *


def hash_func1(key):
    """
    Hash function which return hash value based on
    ord value of letters of the key minus ord value of "a"
    :param key:
    :return: hash value
    """
    hash_val = 0
    for letters in key:
        hash_val += (ord(letters) - ord("a"))
    return hash_val


def hash_func2(key):
    """
    A better hash function which return hash value based on
    ord value of letters of the key minus ord value of "a"
    :param key:
    :return: hash value
    """
    hash_val = 0
    index = 0
    for letters in key:
        hash_val += ((ord(letters) - ord("a")) * (31 ** index))
        index += 1
    return hash_val


def print_map(a_map):
    for word, counter in a_map:  # uses the iter method
        print(word, counter, end=" ")
    print()


def test0():
    table = HashMap(initial_num_buckets=10)
    table.add("to", 1)
    table.add("do", 1)
    table.add("is", 1)
    table.add("to", 2)
    table.add("be", 1)

    print_map(table)

    print("'to' in table?", table.contains("to"))
    print("'to' appears", table.get("to"), "times")
    table.remove("to")
    print("'to' in table?", table.contains("to"))

    print_map(table)


def test_upsizing():
    """
    method tests for rehashing(upsizing) in the table.
    :return:
    """
    print("------In Test 1------", end="\n\n")
    table = HashMap(hash_func=hash_func1, initial_num_buckets=10)
    for num in range(0, 22):
        table.add("ex" + str(num), num)
    print_map(table)


def test_downsizing():
    """
    method tests for rehashing(downsizing) in the table.
    :return:
    """
    print("\n------In Test 2------", end="\n\n")
    table = HashMap(hash_func=hash_func1)
    for num in range(0, 22):
        table.add("ex" + str(num), num)

    print_map(table)

    for num in range(0, 10):
        table.remove("ex" + str(num))

    print_map(table)


def test_same_index():
    """
    method tests for addition and removal of all nodes
    stored at the same location in List.
    :return:
    """
    print("\n------In Test 3------", end="\n\n")
    table = HashMap(hash_func=hash_func1, initial_num_buckets=10)
    for num in range(0, 14):
        table.add("be" + str("u" * num), num)

    print_map(table)

    for num in range(0, 12):
        table.remove("be" + str("u" * num))

    print_map(table)


# def imbalance_test():
#     """
#     uncomment line 9 and move word_count.py into the package before uncommenting this method
#     Method used for testing imbalance in the List
#     :return:
#     """
#     print("\n------Testing Imbalance------")
#
#     capacity = int(input("Enter capacity (-1 for default): "))
#
#     if capacity < 10:
#         h_table = HashMap(hash_func2)
#     else:
#         h_table = HashMap(hash_func2, capacity)
#     filename = input("Enter filename: ")
#
#     word_table = word_count(h_table, filename)
#     print("Imbalance of 1st Hash function is: ", word_table.imbalance())


if __name__ == '__main__':
    test_upsizing()
    test_downsizing()
    test_same_index()
    # imbalance_test()
