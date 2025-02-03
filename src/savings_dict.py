"""
This file contains the dictionary with all sales for items in the shop.

The structure of the dictionary is as follows:

- key : savings code
- value : list containing [ list of items which the savings apply to, parameters for savings ]

Different sales have different structures for the list:
- X% discount; [ [...], X% ]
- Buy X items from list [...] for price of Y items; [ [...], (X,Y) ]
- Buy X items from list [...] for £Y; [ [...], (X,Y,"£") ]
- Buy X items from list [...] and get Y items free; [ [...], (X,Y,0) ]

The dictionary included is from the example in the exercise.
1: Beans; buy 3 for 2
2: Coke; buy 2 for £1
"""

savings = {
    1 : [ [1], (3,2) ],
    2 : [ [2], (2,1,"£") ]
}