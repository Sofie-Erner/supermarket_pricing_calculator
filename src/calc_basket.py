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
    # --- Variables ---
    # subtotal for sum of item prices without savings
    # items: dictionary item number as key and list of occurrences and potential savings code as value
    # savings: sum of savings
    # Total: subTotal minus savings, final price of basket

    """ --- Get dictionary of items & Sub-total --- """
    items, sav_items, subTotal = get_items(shop_basket)
    print("Sub-total: ",subTotal)

    """ --- Get Savings  --- """
    savings = get_savings(sav_items)
    print("Total savings: ",savings)

    """ --- Total price of basket  --- """
    total = round(subTotal - savings,2)
    print("Total to Pay: ",total)
    return 0