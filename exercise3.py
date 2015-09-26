#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car():
    print("We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:")
    raw_input("Please press the Enter/Return key when you are ready to begin.")
    True = "yes" or "y"
    turn_key = raw_input("Is the car silent when you turn the key?")
    if turn_key == True:
        terminals_corroded = raw_input("Are the battery terminals corroded?")
        if terminals_corroded == True:
            print ("Clean terminals and try starting again.")
        else:
            print ("Replace cables and try again.")
    else:
        clicking = raw_input("Does the car make a clicking noise?")
        if clicking == True :
            print("Replace the battery.")
        else:
            crank = raw_input("Does the car crank up but fail to start?")
            if crank == True:
                print("Check spark plug connections.")
            else:
                start_die = raw_input("Does the engine start and then die?")
                if start_die == True:
                    fuel_injection = raw_input("Does your car have fuel injection?")
                    if fuel_injection == True:
                        print("Check to ensure the choke is opening and closing.")
                    else:
                        print("Get it in for service.")
                else:
                    print("It sounds like your enginge does not start up.")
                    print("We should double check the answers to your previous questions. Let's start again.")
                    diagnose_car()



    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    #need Error messages - words other than yes/no/y/n, things that are not words, etc
    #better output messages

diagnose_car()