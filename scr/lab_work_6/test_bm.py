import unittest

from bm_search import *


class TestBMSearch(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_search(self) -> None:
        string = 'abcdefabcdef'
        self.assertEqual(bm_search(string, 'ab'), [0, 6])
        self.assertEqual(bm_search(string, 'k'), [])


if __name__ == "__main__":
    unittest.main()
