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
    shape_sides = raw_input("How many sides does your shape have? ")
    shape_sides = int(shape_sides)
    if shape_sides == 3:
        print("Your shape has %d sides! That is a triangle.") %shape_sides
    elif shape_sides == 4:
        print ("Your shape has %d sides! That is a rectangle.") %shape_sides
    elif shape_sides == 5:
        print ("Your shape has %d sides! That is a pentagon.") %shape_sides
    elif shape_sides == 6:
        print ("Your shape has %d sides! That is a hexagon.") %shape_sides
    elif shape_sides == 7:
        print ("Your shape has %d sides! That is a septagon.") %shape_sides
    elif shape_sides == 8:
        print ("Your shape has %d sides! That is a octogon.") %shape_sides
    elif shape_sides == 9:
        print ("Your shape has %d sides! That is a nonagon.") %shape_sides
    elif shape_sides == 10:
        print ("Your shape has %d sides! That is a decagon.") %shape_sides
    else:
        if shape_sides < 3:
            print ("Error! That is not enough sides. Your shape must have at least 3 sides.")
        elif shape_sides > 10:
            print ("Error! That is too many sides. Your shape must have less than 10 sides.")


    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: number of sides of object (user input)

    Expected Outputs: str from input (name of object)

    Errors: if input >3-10<, produce error message

    !!Error message for if input is str not int?
        print ("raw_input is not a number! Please enter a number.") - loop back to beginning again?
    !!Is there a way to simplify this code?
    !!If input is <3-10<, loop back to beginning of code?

    """

name_that_shape()