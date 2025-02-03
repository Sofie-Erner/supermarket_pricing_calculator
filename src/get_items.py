"""
This file contains the function to calculate the sub-total of a shopping basket.

Input: list of shopping items
Output: sub-total of basket & dictionary with items in basket
"""

import numpy as np

import src
from src.price_dict import prices # get dictionary with prices

# ------ Function to calculate sub-total and get items for shopping basket -----
def get_items(basket):
    subTotal = 0 # subtotal for sum of item prices without savings
    items = {} # dictionary item number as key and list of occurrences and potential savings code as value

    # --- Loop over items in basket ---
    for i in range(0,len(basket)):
        item = basket[i] # current item
        item_number = 0 # current item number

        sale = 0 # switch to 1 if item has sale

        # --- Test for length of item for different categories of pricing
        if type(item) == int: # price per item
            try:
                subTotal += prices[item][0] # add price of item

                item_number = item # save item number

            except Exception as err:
                print("Error for item: ",item_number)
                print(err)
                return -1 

        elif type(item) == tuple: # price per kg
            try:
                # price = X kg * price per kg
                subTotal  += round(item[1] * prices[item[0]][0][0],2)

                item_number = item[0] # save item number

            except Exception as err:
                print("Error for item: ",item_number)
                print(err)
                return -1 

        else: # Unkown
            print("Error for item: ",item)
            print("Unknown item")
            return -1 # return as error

        if item_number in items:
            items[item_number][0] += 1 # increase number of occurrences
        else:
            items[item_number] = [1,0] # add item to list with 1 occurrence and no savings code

        if len(prices[item_number]) == 2: # check for savings code
            items[item_number][1] = prices[item_number][1] # add savings code to dictionary

    return items, subTotal