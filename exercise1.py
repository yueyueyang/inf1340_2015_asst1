#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# Assign a value to the numbers of shares.
shares = 2000

# Assign a value to the price per share.
price = 900

# Assign a value to the percentage of commission.
percentage_of_commission = 0.03

# Calculate the amount of commission by multiplying shares, price, and percentage of commission.
# Assign the result to commission.
commission = shares * price * percentage_of_commission

# Display the commission.
print('The amount of commission is', commission)

# Calculate the total pay by multiplying shares and price and then add commission.
# Assign the result to total_pay.
total_pay = shares * price + commission

# Display the total pay.
print('The total pay for the stock is', total_pay)

# Assign a value to the sold price.
sold_price = 942.75

# Calculate the amount received from the stock by multiplying shares and sold price.
# Assign the result to amount received from the stock.
amount_received_from_the_stock = shares * sold_price

# Display the amount received from the stock.
print('The amount received from the stock is', amount_received_from_the_stock)

# Calculate the amount of the commission after selling the stock by multiplying percentage of commission
# and amount received from the stock.
# Assign the result to commission after selling the stock.
commission_after_selling_the_stock = percentage_of_commission * amount_received_from_the_stock

# Display the commission after selling the stock.
print('The commission after selling the stock is', commission_after_selling_the_stock)

# Calculate the total money left by subtracting the commission after selling the stock
# from the amount received from the stock.
# Assign the result to money left.
money_left = amount_received_from_the_stock - commission_after_selling_the_stock

# Display the amount of money left after paying the commission.
print('The amount of money left after paying the commission', money_left)

# Calculate the money remaining after the stock transaction by subtracting the total pay for the stock
# from the amount of money left.
# Assign the result to money remaining ater the stock transactions.
money_remaining_after_stock_transactions = money_left - total_pay

# Display the profit or loss.
print('Money remaining after the stock transaction is', money_remaining_after_stock_transactions)

# Display the loss.
print('Because money remaining is negative, so Lakshmi has a loss', money_remaining_after_stock_transactions)









