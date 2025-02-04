"""
This file contains the function to calculate the sub-total of a shopping basket.

Input: list of shopping items
Output: sub-total of basket & dictionary with items in basket & dictionary with information for savings
"""

import numpy as np

import src
from src.price_dict import prices # get dictionary with prices

# ------ Function to calculate sub-total and get items for shopping basket -----
def get_items(basket):
    subTotal = 0 # subtotal for sum of item prices without savings

    # dictionary, item number as key and list of occurrences and potential savings code as value
    items = {} # structure: {item_number : [number of occurrences, save_code]}

    # dictionary, collect items under their respective savings codes
    sav_items = {} # structure: {save_code : [[item_number,number of occurrences]]}

    """ --- Loop over items in basket --- """
    for i in range(0,len(basket)):
        item = basket[i] # current item
        item_number = 0 # current item number

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

        """ --- Add to items dictionary --- """
        i_on = 0 # check if item has already occurred in basket

        if item_number in items: # check if item is already in dictionary
            items[item_number][0] += 1 # increase number of occurrences
            i_on = 1 # update check
        else:
            items[item_number] = [1,0] # add item to list with 1 occurrence and no savings code

        """ --- Add to items dictionary --- """
        if len(prices[item_number]) == 2: # check for savings code
            sav_code = prices[item_number][1] # get save_code for item

            items[item_number][1] = sav_code # update items dictionary to include save_code

            if sav_code in sav_items: # check if save_code is already in dictionary
                sav_list = sav_items[sav_code]
                
                if i_on == 1: # if item already in list
                    id = [y[0] for y in sav_list].index(item_number) # index of tuple for item
                    sav_list[id][1] += 1 # increase number of occurrences

                else:
                    sav_list.append([item_number,1]) # add tuple with item_number and 1 occurrence

            else:
                # add save_code to dictionary with item number and 1 occurrence
                sav_items[sav_code] = [[item_number,1]]

    return items, sav_items, subTotal