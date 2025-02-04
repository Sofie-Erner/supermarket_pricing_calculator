import unittest
import os
import sys

path = os.path.abspath(os.getcwd()) # path to directory of script
sys.path.append("../")

import src
from src.get_items import get_items

class get_items_test(unittest.TestCase):
    """
    get_items_test class to test the function
    check against example given in coding exercise
    """

    """ ----- Set up ----- """
    def setUp(self):
        # --- Test result of function and list of keys to compare to 
        test_list = [1,1,1,2,2,(3,0.2)] # list from coding exercise example

        self.subTotal_exp = 3.3 # expected sub-total
        self.items_exp = {1: [3, 1], 2: [2, 2], 3: [1, 0]} # expected items dictionary
        self.savs_expt = {1: [[1, 3]], 2: [[2, 2]]} # expected savings dictionary

        self.items_dict, self.sav_dict, self.subTotal = get_items(test_list) # results of function for test list

    """ ----- Test items dictionary ----- """
    def test_dict_keys(self):
        # --- Test dictionary keys
        self.assertListEqual(list(self.items_dict.keys()),list(self.items_exp.keys()))
        self.assertListEqual(list(self.sav_dict.keys()),list(self.savs_expt.keys()))

    def test_dict_type(self):
        # --- Test outputs are dictionaries
        self.assertIs(type(self.items_dict),dict)
        self.assertIs(type(self.sav_dict),dict)

    """ ----- Test sub-total ----- """
    def test_subTotal(self):
        # --- Test sub-total value
        self.assertEqual(round(self.subTotal,2), self.subTotal_exp)

if __name__ == "__main__":
    unittest.main()