#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

 #This program prints how much money Lakshmi has after buying and selling stock, and paying her broker
 #It then declares if she has a profit or loss, and by how much

 #Test:

 #inputs:
 #expected outputs: After buying and selling stock, and paying her broker both times, Lakshmi has $-25065
 #Because the amount remaining is negative, Lakshmi has a loss of $25065
 #Actual outputs: After buying and selling stock, and paying her broker both times, Lakshmi has $-25065
 #Because the amount remaining is negative, Lakshmi has a loss of $25065

shares = 2000
price = 900
percentage_of_commission = 0.03
commission = shares * price * percentage_of_commission
total_pay = shares * price + commission
sold_price = 942.75
amount_received_from_the_stock = shares * sold_price
commission_after_selling_the_stock = percentage_of_commission * amount_received_from_the_stock
money_left = amount_received_from_the_stock - commission_after_selling_the_stock
money_remaining_after_stock_transactions = money_left - total_pay
loss_amount = money_remaining_after_stock_transactions * -1

print("After buying and selling stock, and paying her broker both times, Lakshmi has $%d") %money_remaining_after_stock_transactions
if money_remaining_after_stock_transactions >0:
    print("Because the amount remaining is positive, Lakshmi has a profit of $%d") %money_remaining_after_stock_transactions
elif money_remaining_after_stock_transactions == 0:
    print("Lakshmi broke even. She did not make a profit or suffer a loss.")
else:
    print("Because the amount remaining is negative, Lakshmi has a loss of $%d") %loss_amount