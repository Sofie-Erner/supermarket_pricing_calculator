"""
This file contains the function to calculate the price of a shopping basket.

Input: list of shopping items
Output: total price of basket
"""
import src
from src.get_items import get_items # function to get dictionary of items and sub-total
from src.get_savings import get_savings # function to calculate savings of basket

# ------ Function to calculate price for a shopping basket -----
def calc_basket(shop_basket):
    print(shop_basket)
    # --- Variables ---
    savings = 0 # sum of savings
    total = 0 # subTotal minus savings, final price of basket

    # subtotal for sum of item prices without savings
    # items: dictionary item number as key and list of occurrences and potential savings code as value

    """ --- Get dictionary of items & Sub-total --- """
    items, sav_items, subTotal = get_items(shop_basket)
        
    print(items)
    print(round(subTotal,2))

    return 0