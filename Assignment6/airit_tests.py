"""
CSCI-603 Autocomplete Lab 5
file: auto-complete.py
description: This program tests the use of stacks and queues to run board/de-board passengers using AiRIT airline
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""
from airit_simulation import *


def test_arguments():
    """
    no arguments provided or one given
    :return: None
    """
    get_arguments("")


def test_one_read_passenger_list():
    """
    file reading function test cases
    no argument given for filename
    wrong file name given which does not exist
    empty string given
    :return: None
    """
    get_passengers_list()
    get_passengers_list("testing....")
    get_passengers_list("")


def test_two_read_passenger_list():
    """
    reading file and printing all passengers
    :return: None
    """
    passenger_list = get_passengers_list("passengers_small.txt")
    for passenger in passenger_list:
        print(passenger)


def test_get_capacity():
    """
    input function for getting capacity
    :return: None
    """
    capacity = get_capacity("test input: ")
    print(capacity)


def test_simulation_one():
    """
    testing with file passengers_small.txt
    taking 2 as gate max capacity and 5 as aircraft max capacity
    aircraft flies 5 times to take the 10 people in a batch of 2 each
    :return: None
    """
    passenger_list = get_passengers_list("passengers_very_small.txt")
    simulation(2, 5, passenger_list)


def test_simulation_two():
    """
    testing with file passengers_small.txt
    taking 5 as gate max capacity and 10 as aircraft max capacity
    aircraft flies 2 times to take the 10 people in a batch of 5 each
    :return: None
    """
    passenger_list = get_passengers_list("passengers_very_small.txt")
    simulation(5, 10, passenger_list)


def test_simulation_three():
    """
    testing with file passengers_small.txt
    taking 7 as gate max capacity and 2 as aircraft max capacity
    aircraft flies 6 times to take the 10 people in a batch of 2 each
    :return: None
    """
    passenger_list = get_passengers_list("passengers_very_small.txt")
    simulation(7, 2, passenger_list)


def test_place_all_passengers_at_gate():
    """
    Testing placing passengers at gate function
    Only allowing 3 passengers at the gate
    :return: None
    """
    passenger_list = get_passengers_list("passengers_very_small.txt")
    gate = Gate(3)
    gate.place_all_passengers(passenger_list)


def test_load_passengers_aircraft():
    """
    testing of loading passengers to aircraft function
    loading passengers from zone 4 to zone 1
    aircraft max size is 5 and gate size is 6
    :return: None
    """
    aircraft = Aircraft(5)
    gate = Gate(6)
    passenger_list = get_passengers_list("passengers_very_small.txt")
    gate.place_all_passengers(passenger_list)
    print("Loading aircraft ....")
    aircraft.load_aircraft(gate)


def test_disembark_passengers_aircraft():
    """
    testing unloading passengers without carry on bag first and then with carry on from zone 1 to 4
    :return:
    """
    aircraft = Aircraft(5)
    gate = Gate(6)
    passenger_list = get_passengers_list("passengers_very_small.txt")
    gate.place_all_passengers(passenger_list)
    print("Loading aircraft.........")
    aircraft.load_aircraft(gate)
    print("disembarking passengers.......")
    aircraft.disembark_passengers()


def test():
    """
    calls all test cases
    :return:
    """
    print("======================Test Case=======================")
    # uncomment to test arguments function
    # test_arguments()
    test_one_read_passenger_list()
    print("======================Test Case=======================")
    test_two_read_passenger_list()
    print("======================Test Case=======================")
    # uncomment to test input for capacity function
    # test_get_capacity()
    print("======================Test Case=======================")
    test_place_all_passengers_at_gate()
    print("======================Test Case=======================")
    test_load_passengers_aircraft()
    print("======================Test Case=======================")
    test_disembark_passengers_aircraft()
    print("======================Test Case=======================")
    test_simulation_one()
    print("======================Test Case=======================")
    test_simulation_two()
    print("======================Test Case=======================")
    test_simulation_three()


if __name__ == '__main__':
    test()
