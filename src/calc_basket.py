"""
This file contains the function to calculate the price of a shopping basket.

Input: list of shopping items
Output: total price of basket

"""

import src
from price_dict import prices # get dictionary with prices
from savings_dict import savings # get dictionary with savings

# ------ Function to calculate price for a shopping basket -----
def calc_basket(shop_basket):
    print(shop_basket)
    return 0