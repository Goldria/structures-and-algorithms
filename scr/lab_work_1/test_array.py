import unittest

import numpy as np

from array_ import *


class TestArray(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_count_elements(self):
        self.assertEqual(count_elements(np.array([1, 1, 1, 1])), 0)
        self.assertEqual(count_elements(np.array([0, 0, 0, 0])), 0)
        self.assertEqual(count_elements(np.array([2, 4, 5, 6])), 1)
        self.assertEqual(count_elements(np.array([2, 4, 6, 8])), 4)
        self.assertEqual(count_elements(np.array([1, 11, 3, 31, 5, 55, 7])), 5)
        self.assertEqual(count_elements(np.array([1, 2, 3, 4, 5, 6, 7])), 5)


if __name__ == "__main__":
    unittest.main()
