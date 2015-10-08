#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# This program helps identify a problem with a car based on yes/no interactive queries

# Inputs: str: "Y"/"N"
# Expected Outputs: str, possible problem with car and instructions
# Errors: if input not "Y"/"N", process finishes without producing answer

# Test1:
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "Y"
# Expected outputs: str: "Are the battery terminals corroded?"
# Actual outputs: str: "Are the battery terminals corroded?"
# Inputs: str: "Y"
# Expected outputs: str: "Clean terminals and try starting again."
# Actual outputs: str: "Clean terminals and try starting again."


# Test2:
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "Y"
# Expected outputs: str: "Are the battery terminals corroded?"
# Actual outputs: str: "Are the battery terminals corroded?"
# Input: str: "N"
# Expected outputs: str: "Replace cables and try again."
# Actual outputs: str: "Replace cables and try again."

# Test3:
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "N"
# Expected outputs: str: "Does the car make a clicking noise?"
# Actual outputs: str: "Does the car make a clicking noise?"
# Inputs: str: "Y"
# Expected outputs: str: "Replace the battery."
# Actual outputs: str: "Replace the battery."

# Test4:
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "N"
# Expected outputs: str: "Does the car make a clicking noise?"
# Actual outputs: str: "Does the car make a clicking noise?"
# Inputs: str: "N"
# Expected outputs: str: "Does the car crank up but fail to start?"
# Actual outputs: str: "Does the car crank up but fail to start?"
# Inputs: str: "Y"
# Expected outputs: str: "Check spark plug connections."
# Actual outputs: str: "Check spark plug connections."

# Test5:
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "N"
# Expected outputs: str: "Does the car make a clicking noise?"
# Actual outputs: str: "Does the car make a clicking noise?"
# Inputs: str: "N"
# Expected outputs: str: "Does the car crank up but fail to start?"
# Actual outputs: str: "Does the car crank up but fail to start?"
# Inputs: str: "N"
# Expected outputs: str: "Does the engine start and then die?"
# Actual outputs: str: "Does the engine start and then die?"
# Inputs: str: "Y"
# Expected outputs: str: "Does your car have fuel injection?"
# Actual outputs: str: "Does your car have fuel injection?"
# Input: str: "Y"
# Expected outputs: str: "Check to ensure the choke is opening and closing."
# Actual outputs: str: "Check to ensure the choke is opening and closing."

# Test6:
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "N"
# Expected outputs: str: "Does the car make a clicking noise?"
# Actual outputs: str: "Does the car make a clicking noise?"
# Inputs: str: "N"
# Expected outputs: str: "Does the car crank up but fail to start?"
# Actual outputs: str: "Does the car crank up but fail to start?"
# Inputs: str: "N"
# Expected outputs: str: "Does the engine start and then die?"
# Actual outputs: str: "Does the engine start and then die?"
# Inputs: str: "Y"
# Expected outputs: str: "Does your car have fuel injection?"
# Actual outputs: str: "Does your car have fuel injection?"
# Inputs: str: "N"
# Expected outputs: str: "Get it in for service."
# Actual outputs: str: "Get it in for service."

# Test7
# We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
# Is the car silent when you turn the key?
# Inputs: str: "N"
# Expected outputs: str: "Does the car make a clicking noise?"
# Actual outputs: str: "Does the car make a clicking noise?"
# Inputs: str: "N"
# Expected outputs: str: "Does the car crank up but fail to start?"
# Actual outputs: str: "Does the car crank up but fail to start?"
# Inputs: str: "N"
# Expected outputs: str: "Does the engine start and then die?"
# Actual outputs: str: "Does the engine start and then die?"
# Inputs: str: "N"
# Expected outputs: str: "Engine is not getting enough fuel. Clean fuel pump."
# Actual outputs: str: "Engine is not getting enough fuel. Clean fuel pump."


def diagnose_car():
#print("We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:")
    silent_when_turn_key = raw_input("Is the car silent when you turn the key?")
    if silent_when_turn_key == "Y":
        terminals_corroded = raw_input("Are the battery terminals corroded?")
        if terminals_corroded == "Y":
            print "Clean terminals and try starting again."
        elif terminals_corroded == "N":
            print "Replace cables and try again."
    elif silent_when_turn_key == "N":
        clicking_noise = raw_input("Does the car make a clicking noise?")
        if clicking_noise == "Y":
            print "Replace the battery."
        elif clicking_noise == "N":
            crank_no_start = raw_input("Does the car crank up but fail to start?")
            if crank_no_start == "Y":
                print "Check spark plug connections."
            elif crank_no_start == "N":
                engine_start_die = raw_input("Does the engine start and then die?")
                if engine_start_die == "Y":
                    fuel_injection = raw_input("Does your car have fuel injection?")
                    if fuel_injection == "Y":
                        print "Get it in for service."
                    elif fuel_injection == "N":
                        print "Check to ensure the choke is opening and closing."
                elif engine_start_die == "N":
                    print "Engine is not getting enough fuel. Clean fuel pump."

#diagnose_car()