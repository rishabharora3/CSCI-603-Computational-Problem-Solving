"""
CSCI-603 Pig dice lab 2
file: pigdice.py
description: This program works on making a pig dice game where the game goes till one player scores a total of 50
author: Karan Ahluwalia, ka7982@rit.edu
author: Zubin Tobias, zt3506@rit.edu
"""
import turtle as t
import math as m
import random as r
from score import Keeper

keeper = Keeper()
SIDE = 100


"""
        initialize the drawing window
       :pre: pos(0,0), heading east, pen up
       :post: pos(0,0), heading east, pen up
       :return: none
"""
def init():
    t.hideturtle()
    t.speed(0)


"""
        Creating a dice using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""

def create_die():

    t.goto(-50, 0)
    t.clear()
    t.pendown()

    for _ in range(4):
        t.forward(SIDE)
        t.left(90)

    t.penup()

"""
        drawing a dot
       :pre: pos(as in calling function), heading east, pen up
       :post: same as :pre:, heading east, pen up
       :return: none
"""

def draw_dot():

    t.pendown()
    t.dot()
    t.penup()


"""
        drawing the dot at a position that would be 
        used as the center of the die using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""

def draw_one_dot():

    t.left(45)
    t.forward(m.sqrt((SIDE * SIDE)+ (SIDE*SIDE))/2)

    draw_dot()

    t.back(m.sqrt((SIDE * SIDE) + (SIDE * SIDE))/2)
    t.right(45)


"""
        drawing the dice representing one on the dice
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_one_dot_die():
    create_die()
    draw_one_dot()
    display_scores()

"""
        drawing the dot at positions that would be 
        used as '2' on the die using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""

def draw_two_dots():
    t.left(45)
    t.forward(m.sqrt((SIDE * SIDE) + (SIDE * SIDE)) / 4)

    draw_dot()

    t.forward(m.sqrt((SIDE * SIDE) + (SIDE * SIDE)) / 2)

    draw_dot()

    t.back((m.sqrt((SIDE * SIDE) + (SIDE * SIDE)) / 4) * 3)
    t.right(45)


"""
        drawing the die representing two on it
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_two_dots_die():
    create_die()
    draw_two_dots()
    display_scores()


"""
        drawing the dots at positions that would be 
        used as '3' on the die using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""

def draw_three_dots():
    create_die()
    draw_one_dot()
    draw_two_dots()



"""
        drawing the die representing three on it
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_three_dots_die():
    create_die()
    draw_three_dots()
    display_scores()


"""
        drawing the dots at positions that would be 
        used as '4' on the die using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_four_dots():
    draw_two_dots()
    t.forward(SIDE)
    t.left(90)
    draw_two_dots()
    t.right(90)
    t.back(SIDE)


"""
        drawing the die representing four on it
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""



def draw_four_dots_die():
    create_die()
    draw_four_dots()
    display_scores()



"""
        drawing the dot at positions that would be 
        used as '5' on the die using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_five_dots():
    draw_one_dot()
    draw_four_dots()


"""
        drawing the die representing five on it
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_five_dots_die():
    create_die()
    draw_five_dots()
    display_scores()


"""
        drawing the dots at positions that would be 
        used as '6' on the die using turtle
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""



def draw_six_dots():
    draw_four_dots()

    t.left(90)
    t.forward(50)
    t.right(90)
    t.forward(25)

    draw_dot()

    t.forward(50)

    draw_dot()

    t.back(75)
    t.left(90)
    t.back(50)
    t.right(90)


"""
        drawing the die representing six on it
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def draw_six_dots_die():
    create_die()
    draw_six_dots()
    display_scores()

"""
        calls the respective functions to display
        the needed numbered die
       :pre: pos(-50,0), heading east, pen up
       :post: pos(-50,0), heading east, pen up
       :return: none
"""


def random_die_call(x, y):
    if -(SIDE/2) <= x <= (SIDE/2) and 0 <= y <= SIDE:
        dienum = r.randint(1, 6)

        if dienum == 1:
            draw_one_dot_die()
            keeper.points = 0
            keeper.switch_player()
        elif dienum == 2:
            draw_two_dots_die()
            keeper.add_points(dienum)
        elif dienum == 3:
            keeper.add_points(dienum)
            draw_three_dots_die()
        elif dienum == 4:
            keeper.add_points(dienum)
            draw_four_dots_die()
        elif dienum == 5:
            keeper.add_points(dienum)
            draw_five_dots_die()
        else:
            keeper.add_points(dienum)
            draw_six_dots_die()

"""
       display the scores of player 1
       :pre: pos(-150,-150), heading east, pen up
       :post: pos(-150,-150), heading east, pen up
       :return: none
"""

def display_player1():
    t.penup()
    t.goto(-150, -150)
    t.color('blue')
    t.write("Player 1 score is:" + str(keeper.score[0]), align='center', font=FONT1)
    t.color('black')
    t.pendown()


"""
       display the scores of player 2
       :pre: pos(150,-150), heading east, pen up
       :post: pos(150,-150), heading east, pen up
       :return: none
"""
def display_player2():
    t.penup()
    t.goto(150, -150)
    t.color('green')
    t.write("Player 2 score is:" + str(keeper.score[1]), align='center', font=FONT1)
    t.color('black')
    t.pendown()


"""
       calls to display scores of both players
       :pre: pos(150,-150), heading east, pen up
       :post: pos(150,-150), heading east, pen up
       :return: none
"""
def display_scores():
    display_player1()
    display_player2()

FONT_SIZE = 12
FONT = ('Arial', FONT_SIZE, 'bold')
FONT1 = ('Arial', FONT_SIZE + 10, 'bold')


"""
       create the hold button
       :pre: pos(0,-80), heading east, pen up
       :post: pos(0,-50), heading east, pen up
       :return: none
"""
def draw_hold_button():
    button = t.Turtle()
    button.hideturtle()
    button.penup()
    button.shape('circle')
    button.fillcolor('red')
    button.penup()
    button.goto(0, -80)
    button.write("HOLD!", align='center', font=FONT)
    button.sety(-50)
    button.onclick(keeper.switch_player)
    button.showturtle()


"""
    The main function.
    :pre: (relative) pos (0,0), heading (east), pen down
    :post: pos (0,-50), heading (east), pen up
    :return: None
    """
def main():

    init()
    create_die()
    t.onscreenclick(random_die_call)
    draw_hold_button()
    t.mainloop()


if __name__ == '__main_':
    main()