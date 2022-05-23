"""
CSCI-603 Autocomplete Lab 5
file: auto-complete.py
description: This program uses stacks and queues to run board/de-board passengers using AiRIT airline
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""


class Passenger:
    _slots_ = "name", "ticket_number", "carry_on", 'link'

    def __init__(self, name, ticket_number, carry_on):
        """
        constructor
        :param name: name of passenger
        :param ticket_number:
        :param carry_on:
        """
        self.name = name
        self.ticket_number = ticket_number
        self.carry_on = carry_on

    def __str__(self):
        return " " + self.name + ", ticket: " + self.ticket_number + ", carry_on: " + self.carry_on
