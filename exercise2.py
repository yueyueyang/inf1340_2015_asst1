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

# Inputs: int: number of sides of object (user input)
# Expected outputs: str stating input and shape name derived from input
# Errors: if input <3 or >10, str "Error"

# Test1:
# How many sides does your shape have?
# Inputs:3
# Expected outputs:triangle
# Actual outputs: str:triangle

# Test2:
# How many sides does your shape have?
# Inputs:4
# Expected outputs:quadrangle
# Actual outputs:quadrangle

# Test3:
# How many sides does your shape have?
# Inputs:5
# Expected outputs:pentagon
# Actual outputs:pentagon

# Test4:
# How many sides does your shape have?
# Inputs:6
# Expected outputs:hexagon
# Actual outputs:hexagon

# Test5:
# How many sides does your shape have?
# Inputs:7
# Expected outputs:septagon
# Actual outputs:septagon

# Test6:
# How many sides does your shape have?
# Inputs:8
# Expected outputs:octogon
# Actual outputs:octogon

# Test7:
# How many sides does your shape have?
# Inputs:9
# Expected outputs:nonagon
# Actual outputs:nonagon

# Test8:
# How many sides does your shape have?
# Inputs:10
# Expected outputs:decagon
# Actual outputs:decagon

# Test9:
# How many sides does your shape have?
# Inputs:1
# Expected outputs:Error
# Actual outputs:Error

# Test10:
# How many sides does your shape have?
# Inputs:11
# Expected outputs:Error
# Actual outputs:Error

shapes = ["point", "line", "open", "triangle", "quadrangle", "pentagon", "hexagon", "septagon", "octogon", "nonagon", "decagon"]


def name_that_shape():
    shape_sides = int(raw_input("How many sides does your shape have? "))
    if shape_sides < 3:
        print "Error"
    elif 10 < shape_sides:
        print "Error"
    else:
        print (shapes[shape_sides])

name_that_shape()