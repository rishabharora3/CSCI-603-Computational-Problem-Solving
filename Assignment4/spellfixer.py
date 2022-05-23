import re
import sys

"""
CSCI-603 Spell Fixer lab 4
file: spellfixer.py
description: This program works on making a pig dice game where the game goes till one player scores a total of 50
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""


def main():
    """
    main method calls the init method
    which inturn starts the program.
    :return: :none:
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
    legal_file_name, keyboard_file = get_arguments()
    legal_words = get_legal_words(legal_file_name)
    keyboard_letters = get_keyboard_letters(keyboard_file)
    startSpellCheck(legal_words, keyboard_letters)


def get_legal_words(file_name):
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


def get_keyboard_letters(file_name):
    """
    Method reads words from file and returns
    dictionary of adjacent keystrokes of a letter
    :param: :file_name:
    :return: :dictionary: keyboard_letters
    """
    keyboard_letters = dict()
    with open(file_name) as file:
        for key_neighbours in file:
            key_neighbours = key_neighbours.strip()
            keyboard_letters[key_neighbours[0]] = set()
            for element in key_neighbours[1:]:
                if element != ' ':
                    keyboard_letters[key_neighbours[0]].add(element)
    return keyboard_letters


def startSpellCheck(legal_words, keyboard_letters):
    """
    The method takes input from user and starts checking spelling
    to find the correct legal word
    :param legal_words:
    :param keyboard_letters:
    :return: :none:
    """
    try:
        text = input("Please enter a word or a sentence:\n")
        while text != "!*!":
            output = ""
            word_list = re.split(" ", text)
            for word in word_list:
                word = remove_punctuation(word)
                output = output + create_legal_words(word.lower(), legal_words, keyboard_letters) + " "
            print(output.strip())
            text = input("Please enter a word or a sentence:\n")
        else:
            print("Bye!")
    except Exception as e:
        print(e)


def remove_punctuation(word):
    """
    removes punctuation from the word
    :param word:
    :return: word without punctuation
    """
    word_with_punctuation = re.split('(\w+)', word)
    return ''.join(word_with_punctuation)


def alreadyExists(word, legal_words):
    """
    checks if the given word is already present in
    the list of legal words and returns True if it is.
    :param word: word to be searched
    :param legal_words: list of legal words
    :return: boolean:
    """
    if word in legal_words:
        return True


def create_legal_words(word, legal_words, keyboard_letters):
    """
    takes in a word to be found in list of legal words,
    and updates the letters in the word iteratively with
    adjacent letters present on keyboard and finds the
    updated word in list and returns the word found in list.
    :param word:
    :param legal_words:
    :param keyboard_letters:
    :return: Word:
    """
    if alreadyExists(word, legal_words):
        return word
    else:
        word_char_list = list(word)
        for index in range(len(word_char_list)):
            character = word_char_list[index]
            for key in keyboard_letters.get(character, ""):
                word_char_list[index] = key
                new_word = "".join(word_char_list)
                if new_word in legal_words:
                    return new_word
            word_char_list[index] = character

        # The logic will swap each adjacent letter and checks against word in list of legal words
        word_char_list = list(word)
        for index in range(len(word_char_list) - 1):
            temp_list = word_char_list.copy()
            x = temp_list[index]
            temp_list[index] = temp_list[index + 1]
            temp_list[index + 1] = x
            if "".join(temp_list) in legal_words:
                return "".join(temp_list)
        # The below code checks, after removing one letter in the word at each index with the list of legal words
        word_char_list = list(word)
        for index in range(len(word_char_list)):
            temp = word_char_list.copy()
            del temp[index]
            if "".join(temp) in legal_words:
                return "".join(temp)
        return word


def get_arguments():
    """"
    takes in input, in the form of argument,
    the file name of dictionary words and
    adjacent keys of a letter.
    """
    if len(sys.argv) < 3:
        print("Usage: python3 spellfixer.py {words-filename} {keyboard-filename}")
        sys.exit()
    else:
        return sys.argv[1], sys.argv[2]


if __name__ == '_main_':
    main()
