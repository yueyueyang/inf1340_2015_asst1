#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def name_that_shape():
    shape_sides = input("How many sides does your shape have? ")
    shape_sides = int(shape_sides)
    if shape_sides == 3:
        print("That is a triangle")
    elif shape_sides == 4:
        print ("That is a rectangle")
    elif shape_sides == 5:
        print ("That is a pentagon")
    elif shape_sides == 6:
        print ("That is a hexagon")
    elif shape_sides == 7:
        print ("That is a septagon")
    elif shape_sides == 8:
        print ("That is a octogon")
    elif shape_sides == 9:
        print ("That is a nonagon")
    elif shape_sides == 10:
        print ("That is a decagon")
    else:
        print ("Error")

    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: number of sides of object (user input)

    Expected Outputs: str from input (name of object)

    Errors: if input >3-10<, produce error message

    """

name_that_shape()