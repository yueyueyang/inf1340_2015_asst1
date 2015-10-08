#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# This program prints how much money Lakshmi has after buying and selling stock, and paying her broker
# It then prints if she has a profit or loss

# Test1:
# Inputs: share = 2000, price = 900, percentage_of_commission = 0.03, sold_price = 942.75
# Expected outputs: float -25065.0, string "loss"
# Actual outputs: float -25065.0, string "loss"

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

print money_remaining_after_stock_transactions