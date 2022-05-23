"""
CSCI-603 Sun Star lab 3
file: sunstar.py
description: This module creates a polygon using fractal curves
author: Karan Ahluwalia, ka7982@rit.edu
author: Zubin Tobias, zt3506@rit.edu
"""

from turtle import *
from math import *
from re import *


def init():
    """
    initialize the drawing window
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading east, pen down
    :return: none
    """
    speed(0)
    hideturtle()
    title("Sun Star Figure")


def draw_side(a: float, b: int, c: float):
    """
    draw a side of the fractal curve
    :pre: pos(0,0), heading north, pen down
    :post: pos(side,0), heading north, pen down
    :return: Sum of length of curve drawn
    """
    side_sum = 0

    if b == 1:
        forward(a)
        side_sum = a
    else:
        forward(a / 4)
        side_sum = side_sum + a / 4
        left(c)
        side_sum = side_sum + draw_side((a / 4) / cos(degree_to_radian(c)), b - 1, c)
        right(2 * c)
        side_sum = side_sum + draw_side((a / 4) / cos(degree_to_radian(c)), b - 1, c)
        left(c)
        forward(a / 4)
        side_sum = side_sum + a / 4

    return side_sum


def draw_polygon(a: float, b: int, c: float, d: int, e: int):
    """
    draw the complete polygon using fractal curve as side
    :pre: pos(0,0), heading north, pen down
    :post: pos(0,0), heading north, pen down
    :return: Sum of length of sides drawn in polygon
    """
    side_sum = 0
    if e > 0:
        side_sum = side_sum + draw_side(a, b, c)
        right(360 / d)
        side_sum = side_sum + draw_polygon(a, b, c, d, e - 1)

    return side_sum


def degree_to_radian(a: float):
    """
    converts degree to radian
    :pre: pos(0,0), heading north, pen down
    :post: pos(0,0), heading north, pen down
    :return: float number, value in radians
    """
    return pi * (a / 180)


def start_program():
    """
    Takes in input from user and returns it after
    passing through error checking method
    :return: values taken in from user(Number of
            Sides, Length of each side, Level
            of curve and angle of deviation)
    """
    side = input("please enter the number of sides the shape will have: ")
    side = error_check_value(side)

    length = input("please enter the length of one side in pixels: ")
    length = error_check_value(length)

    levels = input("please enter the number of levels the figure will have: ")
    levels = error_check_value(levels)

    angle = input("please enter the deviation angle in degrees ")
    angle = error_check_value(angle)

    return int(length), int(levels), int(angle), int(side)


def error_check_value(value):
    """
    Checks if the value entered by user is a valid integer or not
    and returns the value or error message accordingly
    :return: error checked integer value
    """
    while not fullmatch(r'^[1-9]\d*$', value):
        value = input("please enter correct input, the number should be an integer and greater than 0: ")
    return value


def main():
    """
    main method, initializes and call all the functions required for
    computation and output
    :pre: pos(0,0), heading east, pen down
    :post: pos(0,0), heading north, pen down
    :return: none
    """
    a, b, c, d = start_program()
    init()
    left(90)
    print('Total length is: ', draw_polygon(a, b, c, d, d))
    mainloop()


if __name__ == '__main__':
    main()
