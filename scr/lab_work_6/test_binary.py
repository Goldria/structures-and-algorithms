import unittest

from binary_search import *


class TestBinarySearch(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_binary_search(self) -> None:
        arr = [1, 2, 3, 4, 5, 6]
        self.assertEqual(binary_search(arr, 0, len(arr), 4), 3)
        self.assertEqual(binary_search(arr, 0, len(arr), 1), 0)
        self.assertEqual(binary_search(arr, 0, len(arr), 0), -1)
        self.assertEqual(binary_search(arr, 0, len(arr), 0), -1)

    def test_find_matches(self) -> None:
        arr = [1, 2, 3, 3, 4, 5, 6]
        self.assertEqual(find_matches(arr, 4), (1, [4]))
        self.assertEqual(find_matches(arr, 3), (2, [2, 3]))


if __name__ == "__main__":
    unittest.main()
