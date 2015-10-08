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

# Inputs: number of sides of object (user input) in form of int
# Expected outputs: str stating input and shape name derived from input
# Errors: if input: >3-10<, not an integer, no entry at all - produce error message and re-prompt

# Test1:
# How many sides does your shape have?
# Inputs: int: 3
# Expected outputs: str: "Since your shape has 3 sides, it is a triangle!"
# Actual outputs: str: "Since your shape has 3 sides, it is a triangle!"

# Test2:
# How many sides does your shape have?
# Inputs: str: "five"
# Expected outputs: str: "Sorry, I didn't catch that. Please enter a single whole number." (re-prompt)
# Actual outputs: str: "Sorry, I didn't catch that. Please enter a single whole number." (re-prompt)

# Test3:
# How many sides does your shape have?
# Inputs: int: 2
# Expected outputs: str: "Error! That would not make a shape. A shape must have at least three sides." (re-prompt)
# Actual outputs: str: "Error! That would not make a shape. A shape must have at least three sides." (re-prompt)

# Test4:
# How many sides does your shape have?
# Inputs: int: 11
# Expected outputs: str: "Error! That is too many sides. Your shape must have less than 10 sides." (re-prompt)
# Actual outputs: str: "Error! That is too many sides. Your shape must have less than 10 sides." (re-prompt)

# Test5:
# How many sides does your shape have?
# Inputs: float: 3.5
# Expected outputs: str: "Sorry, I didn't catch that. Please enter a single whole number." (re-prompt)
# Actual outputs: str: "Sorry, I didn't catch that. Please enter a single whole number." (re-prompt))

# Test6:
# How many sides does your shape have?
# Inputs: int: 10
# Expected outputs: str: "Since your shape has 10 sides, it is a decagon!"
# Actual outputs: str: "Since your shape has 10 sides, it is a decagon!"

# Test 7:
# How many sides does your shape have?
# Inputs: none
# Expected outputs: str: "Sorry, I didn't catch that. Please enter a single whole number." (re-prompt)
# Actual outputs: str: "Sorry, I didn't catch that. Please enter a single whole number." (re-prompt)


shapes = ["point", "line", "open", "triangle", "quadrangle", "pentagon", "hexagon", "septagon", "octogon", "nonagon", "decagon"]


def name_that_shape():
    while True:
        try:
            shape_sides = int(raw_input("How many sides does your shape have? "))
        # make sure input is int, do not continue until it is
        except ValueError:
            print ("Sorry, I didn't catch that. Please enter a single whole number.")
            continue
        if shape_sides < 3:
            print ("Error! That would not make a shape. A shape must have at least 3 sides.")
            continue
        elif 10 < shape_sides:
            print ("Error! That is too many sides. Your shape must have less than 10 sides.")
            continue
        else:
            print "Since your shape has %d sides, it is a %s!" %(shape_sides, shapes[shape_sides])
            break

name_that_shape()