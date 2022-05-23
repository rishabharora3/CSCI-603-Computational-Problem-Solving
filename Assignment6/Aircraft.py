"""
CSCI-603 Autocomplete Lab 5
file: auto-complete.py
description: This program uses stacks and queues to run board/de-board passengers using AiRIT airline
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""
from cs_stack import Stack


class Aircraft:
    __slots__ = "max_passengers", "stacks", "current_passengers"

    def __init__(self, max_passengers):
        self.max_passengers = int(max_passengers)
        self.stacks = [Stack(), Stack()]
        self.current_passengers = 0

    def get_stack(self, carry_on):
        """
        gets stack based on the carry on bag is true or false
        :param carry_on:
        :return:
        """
        if carry_on == "True":
            return self.stacks[0]
        else:
            return self.stacks[1]

    def get_current_passenger_count(self):
        """
        :return: get current passenger count in aircraft
        """
        return self.current_passengers

    def get_max_passenger_count(self):
        """
        :return: max passenger in aircraft
        """
        return self.max_passengers

    def load_aircraft(self, gate):
        """
        loads aircraft with passengers using while loop
        :param gate: gate object for calling gate class functions
        :return: None
        """
        while self.get_current_passenger_count() < self.get_max_passenger_count():
            self.board_passenger(gate.get_passenger())
            if gate.get_current_passenger_count() == 0:
                print("There are no more passengers at the gate.")
                break
        else:
            print("The aircraft is full.")

    def board_passenger(self, passenger):
        """
        boards one passenger on the aircraft
        :param passenger:
        :return:
        """
        curr_stack = self.get_stack(passenger.carry_on)
        curr_stack.push(passenger)
        print(passenger)
        self.current_passengers += 1

    def disembark_passengers(self):
        """
        disembark passengers using while loop
        :return: None
        """
        while self.get_current_passenger_count() > 0:
            outgoing_passenger = self.disembark_passenger()
            print(outgoing_passenger)

    def disembark_passenger(self):
        """
        disembark a single passenger from stack
        :return: passenger which has been added to stack
        """
        curr_stack = Stack()
        if not self.stacks[1].is_empty():
            curr_stack = self.stacks[1]
        elif not self.stacks[0].is_empty():
            curr_stack = self.stacks[0]
        popped_passenger = curr_stack.peek()
        curr_stack.pop()
        self.current_passengers -= 1
        return popped_passenger
