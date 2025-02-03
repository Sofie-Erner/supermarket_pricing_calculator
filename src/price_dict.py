"""
This file contains the dictionary with all prices for item in the shop.

The structure of the dictionary is as follows:

- key : item numbers
- value : list containing [ price , potential code for savings on item ]

Price has two structures:
1) price per item in £
2) price per kg (£ per unit, unit) as a double

For more information about savings code see "savings_dict.py".

The dictionary included is from the example in the exercise.
1: Beans with price £0.5 per item and savings code 1
2: Coke with price £0.7 per item and savings code 2
3: Oranges with price of £1.99/kg and no savings

"""

prices = {
    1: [ 0.5, 1 ], # potatoes
    2: [ 0.7, 2 ], # beans
    3: [ (1.99, "kg") ] # oranges
}