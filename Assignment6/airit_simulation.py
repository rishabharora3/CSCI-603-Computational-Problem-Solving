"""
CSCI-603 Autocomplete Lab 5
file: auto-complete.py
description: This program uses stacks and queues to run board/de-board passengers using AiRIT airline
author: Rishabh Arora, ra8851@rit.edu
author: Karan Ahluwalia,ka7982@rit.edu
"""
import sys

from Passenger import Passenger
from re import fullmatch

from lab7.Aircraft import Aircraft
from lab7.Gate import Gate


def main(args):
    """
    driver function runs the simulation of the program, takes input and gets arguments
    :param args:
    :return:
    """
    passenger_file_name = get_arguments(args)
    all_passenger_list = get_passengers_list(passenger_file_name)
    gate_max = get_capacity("Gate capacity: ")
    aircraft_max = get_capacity("Aircraft capacity: ")
    simulation(gate_max, aircraft_max, all_passenger_list)


def get_arguments(args):
    """
    arguments entered by user passenger file name
    :param args: arguments
    :return: passenger file name
    """
    if len(args) < 2:
        print("Usage: python3 airit_simulation.py {filename}")
        sys.exit()
    else:
        return sys.argv[1]


def get_passengers_list(passenger_file_name=""):
    """
    reads file and gets the passenger list
    :param passenger_file_name:
    :return: passenger list
    """
    all_passenger_list = list()
    try:
        with open(passenger_file_name) as file:
            for passenger in file:
                data_passenger = passenger.split(",")
                all_passenger_list.append(Passenger(data_passenger[0], data_passenger[1], data_passenger[2][:-1]))
    except OSError or TypeError:
        print(f"File not found: {passenger_file_name}")
    return all_passenger_list


def get_capacity(input_str):
    """
    takes input from the user for capacity of gate and aircraft
    :param input_str: user input string
    :return:
    """
    gate_max = input(input_str)
    while not fullmatch(r'^[1-9]\d*$', gate_max):
        gate_max = input("Please enter correct input, the number should be an integer and greater than 0: ")
    return int(gate_max)


def simulation(gate_max, aircraft_max, passenger_list):
    """
    main function which runs the simulation of the program
    :param gate_max: max capacity of gate
    :param aircraft_max: max capacity of aircraft
    :param passenger_list: all passenger list
    :return: None
    """
    gate = Gate(gate_max)
    aircraft = Aircraft(aircraft_max)
    print("Beginning simulation...")

    while len(passenger_list) > 0:
        print("Passengers are lining up at the gate...")
        passenger_list = gate.place_all_passengers(passenger_list)
        while gate.get_current_passenger_count() > 0:
            print("Passengers are boarding the aircraft...")
            aircraft.load_aircraft(gate)
            print("Ready for taking off ...")
            print("The aircraft has landed.")
            print("Passengers are disembarking...")
            aircraft.disembark_passengers()
    else:
        print("Simulation complete; all passengers are at their destination!")


if __name__ == '__main__':
    main(sys.argv)
