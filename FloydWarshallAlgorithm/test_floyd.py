"""
Test module for main.py
"""

import unittest, sys, itertools
from main import floyd_rec

NO_PATH = sys.maxsize

class TestFloyd(unittest.TestCase):
    """
    Test the function floyd rec from module main.py
    """
    def test_floyd(self):
        self.assertEqual(floyd_rec([
                            [0, 7, NO_PATH, 8], 
                            [NO_PATH, 0, 5, NO_PATH],
                            [NO_PATH, NO_PATH, 0, 2],
                            [NO_PATH, NO_PATH, NO_PATH, 0]
                            ]), 
                            [
                            [0, 7, 12, 8], 
                            [9223372036854775808, 0, 5, 7], 
                            [9223372036854775808, 9223372036854775808, 0, 2], 
                            [9223372036854775808, 9223372036854775808, 9223372036854775808, 0]
                            ])

if __name__ == '__main__':
    unittest.main()
    print("Everything passed")