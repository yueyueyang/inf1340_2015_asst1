#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

shapes = {0:" ", 1:"point", 2:"line", 3:"triangle", 4:"quadrangle", 5:"pentagon", 6:"hexagon", 7:"septagon", 8:"octogon", 9:"nonagon", 10:"decagon"}
def name_that_shape():
    shape_sides = raw_input("How many sides does your shape have? ")
    if len(shape_sides) == 0:
        print ("You need to enter a number. How many sides does your shape have?")
    else:
        try:
            shape_sides = int(shape_sides)
        except ValueError:
            print ("That is a word, not a number! You need to enter a number.")
            #loop here back to raw_input so does not continue with word and count number of letters
    if 3 <= shape_sides <= 10:
        print "Your shape has %d sides! That is a %s." %(shape_sides, shapes[shape_sides])
    elif shape_sides == 0:
        print("Error! That is no sides at all. Your shapes must have at least 3 sides.")
    elif 1 <= shape_sides < 3:
        print ("Error! That is not enough sides. Your shape must have at least 3 sides.")
    elif 10 < shape_sides:
        print ("Error! That is too many sides. Your shape must have less than 10 sides.")

name_that_shape()

 #For a given number of sides in a regular polygon, returns the shape name

#Inputs: number of sides of object (user input)

#Expected Outputs: str from input (name of object)

#Errors: if input >3-10<, produce error message

#!!Error message for if input is str not int? - loop back to beginning again?
#!!If input is <3-10<, loop back to beginning of code?

