#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# This program determines shape name depending on the number of sides in a polygon

# Inputs: str: number of sides of object (user input)
# Expected outputs: str stating input and shape name derived from input
# Errors: if input <3 or >10, str "Error"

# Test1:
# How many sides does your shape have?
# Inputs:str "3"
# Expected outputs: str: "triangle"
# Actual outputs: str: "triangle"

# Test2:
# How many sides does your shape have?
# Inputs: str "4"
# Expected outputs: str: "quadrilateral"
# Actual outputs:str: "quadrilateral"

# Test3:
# How many sides does your shape have?
# Inputs: str: "5"
# Expected outputs: str: "pentagon"
# Actual outputs: str: "pentagon"

# Test4:
# How many sides does your shape have?
# Inputs: str: "6"
# Expected outputs: str: "hexagon"
# Actual outputs: str: "hexagon"

# Test5:
# How many sides does your shape have?
# Inputs: str: "7"
# Expected outputs: str: "heptagon"
# Actual outputs: str: "heptagon"

# Test6:
# How many sides does your shape have?
# Inputs: str: "8"
# Expected outputs: str: "octogon"
# Actual outputs: str: "octogon"

# Test7:
# How many sides does your shape have?
# Inputs: str: "9"
# Expected outputs: str: "nonagon"
# Actual outputs: str: "nonagon"

# Test8:
# How many sides does your shape have?
# Inputs: str: "10"
# Expected outputs: str: "decagon"
# Actual outputs: str: "decagon"

# Test9:
# How many sides does your shape have?
# Inputs: str: "1"
# Expected outputs: str: "Error"
# Actual outputs: str: "Error"

# Test10:
# How many sides does your shape have?
# Inputs: str: "11"
# Expected outputs: str: "Error"
# Actual outputs: str: "Error"


def name_that_shape():
    shape_sides = raw_input("How many sides does your shape have? ")
    if shape_sides == "3":
        print "triangle"
    elif shape_sides == "4":
        print"quadrilateral"
    elif shape_sides == "5":
        print "pentagon"
    elif shape_sides == "6":
        print "hexagon"
    elif shape_sides == "7":
        print "heptagon"
    elif shape_sides == "8":
        print "octagon"
    elif shape_sides == "9":
        print "nonagon"
    elif shape_sides == "10":
        print "decagon"
    else:
        print "Error"

#name_that_shape()