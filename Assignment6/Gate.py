"""
CSCI-603 Autocomplete Lab 5
file: auto-complete.py
description: This program uses stacks and queues to run board/de-board passengers using AiRIT airline
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""
from cs_queue import Queue


class Gate:
    __slots__ = "current", "max_size", "zones"

    def __init__(self, max_size):
        """
        constructor
        :param max_size: max size provided by user
        """
        self.max_size = int(max_size)
        self.current = 0
        self.zones = [Queue(), Queue(), Queue(), Queue()]

    def get_queue(self, zone_number):
        """
        :param zone_number:
        :return: return queue based on queue
        """
        return self.zones[zone_number - 1]

    def get_max_pass_count(self):
        """
        :return: get max passenger count on gate
        """
        return self.max_size

    def get_current_passenger_count(self):
        """
        :return: get current passenger count on gate
        """
        return self.current

    def place_all_passengers(self, passenger_list):
        """
        place all passengers in the queue
        :param passenger_list:
        :return:
        """
        while self.get_current_passenger_count() < self.get_max_pass_count():
            self.place_passenger(passenger_list[0])
            print(passenger_list[0])
            passenger_list = passenger_list[1:]
            if len(passenger_list) == 0:
                print("The last passenger is in line!")
                break
        else:
            print("The gate is full; remaining passengers must wait.")
        return passenger_list

    def place_passenger(self, passenger):
        """
        place a single passenger in the queue
        :param passenger: passenger to queue
        :return: None
        """
        curr_queue = self.get_queue(int(passenger.ticket_number[0]))
        curr_queue.enqueue(passenger)
        self.current = self.current + 1

    def get_passenger(self):
        """
        gets passenger from queue 4 to 1 based on their capacity
        :return:
        """
        zone = Queue()
        if not self.zones[3].is_empty():
            zone = self.zones[3]
        elif not self.zones[2].is_empty():
            zone = self.zones[2]
        elif not self.zones[1].is_empty():
            zone = self.zones[1]
        elif not self.zones[0].is_empty():
            zone = self.zones[0]
        passenger = zone.peek()
        zone.dequeue()
        self.current = self.current - 1
        return passenger
