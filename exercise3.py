#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

    #This program helps identify a problem with a car based on yes/now interactive queries

    #Inputs: str, 'yes' or 'no'
    #Expected Outputs: str, possible problem with car and instructions
    #Errors: if input not 'yes' or 'no', tell user it is incorrect and prompt for new, correct, answer

    #YUE: THIS IS WHAT I THINK WE STILL NEED TO PUT IN:
    #y/n as option: I am not sure if add y/n as an option either. In the example provided in the instruction, it uses y/n.
    #Maybe yes/no is also ok.

    #better output messages: i think providing the same output messages as the instructions showed is fine.

    #In the test7, after entering the fourth no, it shows "Engine is not getting enough fuel. Clean fuel pump."
    #I don't see there is such a scenario in the decision tree. Do you think if we need to change that part or not?

    #continue loops back to beginning - make it loop make to sub question? yea, i also find this problem when doing the tests.
    #but i don't know how to fix it.
    # Also i didn't write the repeated begining quesitons when there was an error showed up in the output messages
    # for both excercise 2 and 3.Do you think that we need to add those beginning quesitons in the end of the tests?


#Test1:
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:yes
#Expected outputs:Are the battery terminals corroded?
#Actual outputs:Are the battery terminals corroded?
#Inputs:yes
#Expected outputs:Clean terminals and try starting again.
#Actual outputs:Clean terminals and try starting again.

#Test2:
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:yes
#Expeted outputs:Are the battery terminals corroded?
#Actual outputs:Are the battery terminals corroded?
#Input: no
#Expected outputs:Replace cables and try again.
#Actual outputs:Replace cables and try again.

#Test3:
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:no
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:yes
#Expected outputs:Replace the battery.
#Actual outputs:Replace the battery.

#Test4:
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:no
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:no
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:yes
#Expected outputs:Check spark plug connections.
#Actual outputs: Check spark plug connections.

#Test5:
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:no
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:no
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:no
#Expected outputs:Does the engine start and then die?
#Actual outputs:Does the engine start and then die?
#Inputs:yes
#Expected outputs:Does your car have fuel injection?
#Actual outputs:Does your car have fuel injection?
#Input:yes
#Expected outputs:Check to ensure the choke is opening and closing.
#Actual outputs:Check to ensure the choke is opening and closing.

#Test6:
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:no
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:no
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:no
#Expected outputs:Does the engine start and then die?
#Actual outputs:Does the engine start and then die?
#Inputs:yes
#Expected outputs:Does your car have fuel injection?
#Actual outputs:Does your car have fuel injection?
#Inputs:no
#Expected outputs:Get it in for service.
#Actual outputs:Get it in for service.

#Test7
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:no
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:no
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:no
#Expected outputs:Does the engine start and then die?
#Actual outputs:Does the engine start and then die?
#Inputs:no
#Expected outputs:Engine is not getting enough fuel. Clean fuel pump.
#Actual outputs:Engine is not getting enough fuel. Clean fuel pump.

#Test8
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:y
#Expected outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.
#Actual outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.

#Test9
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Input:'yes'
#Expected outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.
#Actual outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.


#Test10
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:n
#Expected outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.
#Actual outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.


#Test11
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:
#Expected outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.
#Actual outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.

#Test12
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:yes
#Expected outputs:Are the battery terminals corroded?
#Actual outputs:Are the battery terminals corroded?
#Inputs:y
#Expected outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.
#Actual outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.

#Test13
#We are going to help you trouble shoot your car! Please answer 'yes' or 'no' to the following questions:
#Please press the Enter/Return key when you are ready to begin.
#Inputs: Enter/Return
#Expected outputs:Is the car silent when you turn the key?
#Actual outputs:Is the car silent when you turn the key?
#Inputs:no
#Expected outputs:Does the car make a clicking noise?
#Actual outputs:Does the car make a clicking noise?
#Inputs:no
#Expected outputs:Does the car crank up but fail to start?
#Acutal outputs:Does the car crank up but fail to start?
#Inputs:y
#Expected outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.
#Acutal outputs:Sorry, I didn't catch that! Please type 'yes' or 'no' for your answer.


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
                        print("Engine is not getting enough fuel. Clean fuel pump.")
                        break
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

diagnose_car()