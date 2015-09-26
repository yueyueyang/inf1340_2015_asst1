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
    while True:
        turn_key = raw_input("Is the car silent when you turn the key?")
        if turn_key == "yes":
            terminals_corroded = raw_input("Are the battery terminals corroded?")
            if terminals_corroded == "yes":
                print ("Clean terminals and try starting again.")
                break
            elif terminals_corroded == "no":
                print ("Replace cables and try again.")
                break
            else:
                print("Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.")
                continue
        elif turn_key == "no":
            clicking = raw_input("Does the car make a clicking noise?")
            if clicking == "yes":
                print("Replace the battery.")
                break
            elif clicking == "no":
                crank = raw_input("Does the car crank up but fail to start?")
                if crank == "yes":
                    print("Check spark plug connections.")
                    break
                elif crank == "no":
                    start_die = raw_input("Does the engine start and then die?")
                    if start_die == "yes":
                        fuel_injection = raw_input("Does your car have fuel injection?")
                        if fuel_injection == "yes":
                            print("Check to ensure the choke is opening and closing.")
                            break
                        elif fuel_injection == "no":
                            print("Get it in for service.")
                            break
                        else:
                            print("Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.")
                            continue
                    elif start_die == "no":
                        print("It sounds like your enginge does not start up.")
                        print("We should double check the answers to your previous questions. Let's start again.")
                        continue
                    else:
                        print("Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.")
                        continue
                else:
                    print("Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.")
                    continue
            else:
                print("Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.")
                continue
        else:
            print("Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.")
            continue


    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.

    Inputs:

    Expected Outputs:

    Errors:

    """

    #y/n as option
    #better output messages
    #continue loops back to beginning - make it loop make to sub question?

diagnose_car()