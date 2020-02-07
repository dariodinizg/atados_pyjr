import os
import sys
sys.path.append(os.getcwd())

import unittest
import calculator

class TestStockCalculator(unittest.TestCase):

    def test_best_sell(self):
        test_case = [7,1,5,3,6,4]
        self.assertEqual(calculator.stock_calculator(test_case), 5)

    def test_best_sell2(self):
        test_case = [7,6,4,3,1]
        self.assertEqual(calculator.stock_calculator(test_case), 0)