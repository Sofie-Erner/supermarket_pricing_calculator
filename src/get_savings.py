"""
This file contains the function to calculate the savings of a shopping basket.

Input: list of items with occurrences and saving codes
Output: total savings
"""
import math
import numpy as np

import src
from src.price_dict import prices # get dictionary with prices
from src.savings_dict import savings # get dictionary with savings

# ------ Function to calculate savings for shopping basket -----
def get_savings(sav_items):
    total = 0 # total savings

    """ --- Loop over applicable savings codes --- """
    for save_code in sav_items:
        items = sav_items[save_code] # get list of relevant item_numbers and occurrences
        
        try:
            sav = savings[save_code] # Get savings type from dictionary

        except Exception as err: # if savings code not in dictionary
            print("Error for savings code: ",save_code)
            print(err)
            return -1 

        if type(sav[1]) == float: # percentage discount
            # price * occurrences * % discount
            # price = prices[item[0]][0]
            # occurrences = item[1]
            total += sum([ prices[item[0]][0] * item[1] * sav[1] for item in items ])

        elif type(sav[1]) == tuple: #
            X = sav[1][0] # Buy X item from list [...]
            Y = sav[1][1] # sales savings items 

            N = sum([ item[1] for item in items ]) # total number of items
            div_num = math.floor(N/X) # the number of times X divides N

            price_list = [ [prices[item[0]][0],item[1]] for item in items ] # list of prices for items
            temp_prices = [y[0] for y in price_list] # list with only prices
            id_sort =  np.argsort(temp_prices) # sorted list with indices in order of smallest price
            id_sort = [ int(id) for id in id_sort for i in range(0,price_list[id][1])] # number of indices using number of occurrences

            # --- Buy X items from list [...] for price of Y items ---
            if len(sav[1]) == 2:
                # remove the cheapest (X-Y) items 
                total += sum([price_list[id_sort[i]][0] for i in range(0,(X-Y)*div_num)])

            # --- Buy X items from list [...] for £Y ---
            elif len(sav[1]) == 3 and sav[1][2] == "£":
                # subtract the prices of the items which are discounted and add £Y
                total += sum([price_list[id_sort[i]][0] for i in range(0,X*div_num)]) - Y*div_num

        else: # savings type not included yet
            print("Error for savings code: ",save_code)
            return -1 

    return round(total,2)



