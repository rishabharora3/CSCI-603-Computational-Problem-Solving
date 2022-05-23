"""
CSCI-603 Write a Meme Lab 1
file: write_a_meme.py
description: This program draws the meme 'GO TOM FLY' using turtle functions
language: python3
author: Rishabh Arora, ra8851@rit.edu
"""

import turtle
import math

# global constants for window dimensions
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 1000
# global constant for moving back coordinates on x axis,
DRAW_START = 400
# global constants for character dimensions
CHAR_LEN = 80
CHAR_SPACING = 20
# constants for defining angles
RIGHT_ANGLE = 90
STRAIGHT_ANGLE = 180


def init() -> None:
    """
    Initialize for drawing.  (0,0) is at the origin
    :pre: pos (0,0), heading (east), down
    :post: pos (0,0), heading (east), up
    :return: None
    """
    turtle.setup(WINDOW_WIDTH, WINDOW_HEIGHT, 0, 0)
    turtle.up()
    # moving back to fit the text in the screen
    turtle.back(DRAW_START)
    turtle.setheading(0)
    turtle.title('write_a_meme')
    turtle.speed(6)


def defaultSpace() -> None:
    """
    Creates a default space between two words
    :pre: left corner at bottom(start of default space), heading (east), pen up
    :post: right corner at bottom(end of default space), heading (east), pen up
    :return: None
    """
    turtle.forward(CHAR_LEN * (3 / 4))


def charSpace() -> None:
    """
    Creates a space of CHAR_SPACING size between names
    :pre: left corner at bottom(start of space), heading (east), pen up
    :post: right corner at bottom(end of space), heading (east), pen up
    :return: None
    """
    turtle.forward(CHAR_SPACING)


def drawG() -> None:
    """
    Draws a character 'G'
    :pre: left corner at bottom(start of character G), heading (east), pen up
    :post: right corner at bottom(end of character G), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.penup()
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 2)
    turtle.right(RIGHT_ANGLE)
    turtle.pendown()
    turtle.forward(CHAR_LEN / 4)
    turtle.penup()
    turtle.right(STRAIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 4)
    turtle.right(RIGHT_ANGLE)
    turtle.pendown()
    turtle.forward(CHAR_LEN / 2)
    turtle.left(RIGHT_ANGLE)
    turtle.back(CHAR_LEN)
    turtle.forward(CHAR_LEN)
    turtle.penup()


def drawO() -> None:
    """
    Draws a character 'O'
    :pre: left corner at bottom(start of character O), heading (east), pen up
    :post: right corner at bottom(end of character O), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.left(RIGHT_ANGLE)
    turtle.back(CHAR_LEN)
    turtle.penup()
    turtle.forward(CHAR_LEN)


def drawT() -> None:
    """
    Draws a character 'T'
    :pre: left corner at bottom(start of character T), heading (east), pen up
    :post: right corner at bottom(end of character T), heading (east), pen up
    :return: None
    """
    turtle.forward(CHAR_LEN / 2)
    turtle.pendown()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.right(RIGHT_ANGLE)
    turtle.penup()
    turtle.back(CHAR_LEN / 2)
    turtle.pendown()
    turtle.forward(CHAR_LEN)
    turtle.penup()
    turtle.back(CHAR_LEN / 2)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 2)


def drawM() -> None:
    """
    Draws a character 'M'
    :pre: left corner at bottom(start of character M), heading (east), pen up
    :post: right corner at bottom(end of character M), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.right(150)
    turtle.forward(CHAR_LEN * (2 / math.sqrt(3)))  # using 30,60,90 degree triangle diagonal formula
    turtle.left(120)
    turtle.forward(CHAR_LEN * (2 / math.sqrt(3)))
    turtle.right(150)
    turtle.forward(CHAR_LEN)
    turtle.left(RIGHT_ANGLE)
    turtle.penup()


def drawF() -> None:
    """
    Draws a character 'F'
    :pre: left corner at bottom(start of character F), heading (east), pen up
    :post: right corner at bottom(end of character F), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN * (3 / 4))
    turtle.penup()
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 2)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 2)
    turtle.pendown()
    turtle.forward(CHAR_LEN * (1 / 4))
    turtle.penup()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 2)
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN * (3 / 4))


def drawL() -> None:
    """
    Draws a character 'L'
    :pre: left corner at bottom(start of character L), heading (east), pen up
    :post: right corner at bottom(end of character L), heading (east), pen up
    :return: None
    """
    turtle.pendown()
    turtle.left(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN)
    turtle.penup()
    turtle.back(CHAR_LEN)
    turtle.right(RIGHT_ANGLE)
    turtle.pendown()
    turtle.forward(CHAR_LEN * (3 / 4))
    turtle.penup()


def drawY() -> None:
    """
    Draws a character 'Y'
    :pre: left corner at bottom(start of character Y), heading (east), pen up
    :post: right corner at bottom(end of character Y), heading (east), pen up
    :return: None
    """
    turtle.forward(CHAR_LEN / 4)
    turtle.left(RIGHT_ANGLE)
    turtle.pendown()
    turtle.forward(CHAR_LEN / 2)
    turtle.left(45)
    turtle.forward(CHAR_LEN * (3 / 4))
    turtle.penup()
    turtle.back(CHAR_LEN * (3 / 4))
    turtle.right(RIGHT_ANGLE)
    turtle.pendown()
    turtle.forward(CHAR_LEN * (3 / 4))
    turtle.penup()
    turtle.back(CHAR_LEN * (3 / 4))
    turtle.left(45)
    turtle.back(CHAR_LEN / 2)
    turtle.right(RIGHT_ANGLE)
    turtle.forward(CHAR_LEN / 4)


def drawMeme() -> None:
    """
    Draw the meme "GO TOM FLY"
    :pre: left corner at bottom(start of character G), heading (east), pen up
    :post: right corner with word space at bottom(end of character Y), heading (east), pen up
    :return: None
    """
    drawGo()

    drawTom()

    drawFly()


def drawGo():
    """
    Draw the word Go
    :pre: left corner at bottom(start of character G), heading (east), pen up
    :post: right corner with word space at bottom(end of character O), heading (east), pen up
    :return: None
    """
    drawG()
    charSpace()  # giving space between 2 characters
    drawO()
    defaultSpace()  # giving space between words


def drawTom():
    """
    Draw the word Tom
    :pre: left corner at bottom(start of character T), heading (east), pen up
    :post: right corner with word space at bottom(end of character M), heading (east), pen up
    :return: None
    """
    drawT()
    charSpace()
    drawO()
    charSpace()
    drawM()
    defaultSpace()


def drawFly():
    """
    Draw the word Fly
    :pre: left corner at bottom(start of character F), heading (east), pen up
    :post: right corner with word space at bottom(end of character Y), heading (east), pen up
    :return: None
    """
    drawF()
    charSpace()
    drawL()
    charSpace()
    drawY()
    defaultSpace()


def main() -> None:
    """
    The main function.
    :pre: (relative) pos (0,0), heading (east), pen down
    :post: right corner with word space at bottom(end of character Y), heading (east), pen up
    :return: None
    """
    # setting up turtle
    init()
    # drawing the meme
    drawMeme()
    # avoiding closure of screen once the figure is drawn
    turtle.done()


if __name__ == '__main__':
    main()
