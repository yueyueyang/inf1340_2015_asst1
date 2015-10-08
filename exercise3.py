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

#Test1:
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:Y
#Expected outputs:Are the battery terminals corroded?
#Actual outputs:Are the battery terminals corroded?
#Inputs:Y
#Expected outputs:Clean terminals and try starting again.
#Actual outputs:Clean terminals and try starting again.


#Test2:
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:Y
#Expeted outputs:Are the battery terminals corroded?
#Actual outputs:Are the battery terminals corroded?
#Input: N
#Expected outputs:Replace cables and try again.
#Actual outputs:Replace cables and try again.

#Test3:
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:N
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:Y
#Expected outputs:Replace the battery.
#Actual outputs:Replace the battery.

#Test4:
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:N
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:N
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:Y
#Expected outputs:Check spark plug connections.
#Actual outputs: Check spark plug connections.

#Test5:
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:N
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:N
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:N
#Expected outputs:Does the engine start and then die?
#Actual outputs:Does the engine start and then die?
#Inputs:Y
#Expected outputs:Does your car have fuel injection?
#Actual outputs:Does your car have fuel injection?
#Input:Y
#Expected outputs:Check to ensure the choke is opening and closing.
#Actual outputs:Check to ensure the choke is opening and closing.

#Test6:
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:N
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:N
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:N
#Expected outputs:Does the engine start and then die?
#Actual outputs:Does the engine start and then die?
#Inputs:Y
#Expected outputs:Does your car have fuel injection?
#Actual outputs:Does your car have fuel injection?
#Inputs:N
#Expected outputs:Get it in for service.
#Actual outputs:Get it in for service.

#Test7
#We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:
#Please press any key when you are ready to begin. And remember to type your answer as a capital letter!
#Inputs: any key
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:N
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:N
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:N
#Expected outputs:Does the engine start and then die?
#Actual outputs:Does the engine start and then die?
#Inputs:N
#Expected outputs:Engine is not getting enough fuel. Clean fuel pump.
#Actual outputs:Engine is not getting enough fuel. Clean fuel pump.


def diagnose_car():
    print("We are going to help you trouble shoot your car! Please answer 'Y' or 'N' to the following questions:")
    # make sure user knows how to format answer to make code work
    raw_input("Please press any key when you are ready to begin. And remember to type your answer as a capital letter!")
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
                        print "Check to ensure the choke is opening and closing."
                    elif fuel_injection == "N":
                        print "Get it in for service."
                elif engine_start_die == "N":
                    print "Engine is not getting enough fuel. Clean fuel pump."

diagnose_car()