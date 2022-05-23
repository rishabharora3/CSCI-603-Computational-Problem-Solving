"""
CSCI-603 Autocomplete Lab 5
file: auto-complete.py
description: This program searches a word based on given prefix
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""

import sys
from bsearch import binary_search
from sort import merge_sort


def main():
    """
    start of program, driver function
    :return: None
    """
    init()


def init():
    """
    this method initializes the program, and runs
    all the methods needed to start the logic,
    including argument reading, initialization of
    data structures from files and start the search
    :return: :none:
    """
    words_filename = get_arguments()
    unsorted_words = get_words(words_filename)
    sorted_words = merge_sort(unsorted_words)
    print("The sorted list:", sorted_words)
    print("""Welcome to Auto-complete!
    Usage: Enter a prefix to auto-complete.
    Entering nothing will print the first word in the sorted list.
    Enter <QUIT> to exit.""")
    auto_complete(sorted_words)


def get_arguments():
    """"
    takes in input, in the form of argument,
    the file name of valid words
    """
    if len(sys.argv) < 2:
        print("Usage: python3 auto-complete.py {words-filename}")
        sys.exit()
    else:
        return sys.argv[1]


def get_words(file_name):
    """
    Method reads words from file and returns
    the words from in list
    :param: :file_name:
    :return: :list: legal_words
    """
    legal_words = list()
    with open(file_name) as file:
        for word in file:
            legal_words.append(word.strip().lower())
    return legal_words


def auto_complete(sorted_words):
    """
    main logic of the program to manage autocompletion using binary search and
    linear search
    :param sorted_words:
    :return:
    """
    input_prefix = input("Enter a prefix to search for:\n")
    while input_prefix != "<QUIT>":
        prefix = input_prefix
        initial_index = search(sorted_words, prefix)
        if initial_index == -1:
            print("No match")
            input_prefix = input("Enter a prefix to search for:\n")
        else:
            itr = initial_index
            while itr != -1:
                print(sorted_words[itr])
                input_prefix = input("Enter a prefix to search for:\n")
                if input_prefix == "":
                    itr = get_next_word(sorted_words, itr, prefix)
                    if itr == -1:
                        itr = initial_index
                else:
                    break
    else:
        print("Exiting Auto-complete! Good bye.")


def search(sorted_list, value):
    """
    This method will call binary search method and returns the index.
    :param  sorted_list:
    :param  value:
    :return index:
    """
    index = binary_search(sorted_list, value, 0, len(sorted_list) - 1)
    if not sorted_list[index][0:len(value)] == value:
        return -1
    else:
        return index


def get_next_word(sorted_words, itr, input_prefix):
    """
    get next word for linear search
    :param sorted_words: word list
    :param itr: iterator
    :param input_prefix: prefix user entered
    :return: index
    """
    if (itr + 1 < len(sorted_words)) and sorted_words[itr + 1][0:len(input_prefix)] == input_prefix:
        return itr + 1
    return -1


if __name__ == '__main__':
    main()
