import unittest

from tree_search import *


class TestTreeSearch(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BST()

    def test_insert(self) -> None:
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(7)
        self.assertEqual(self.tree.root.key, 5)
        self.assertEqual(self.tree.root.left.key, 4)
        self.assertEqual(self.tree.root.right.key, 7)

    def test_search(self) -> None:
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(7)
        self.assertEqual(self.tree.search(4), True)
        self.assertEqual(self.tree.search(6), False)

    def test_delete(self) -> None:
        self.tree.insert(5)
        self.tree.insert(4)
        self.tree.insert(7)
        self.tree.insert(10)
        self.tree.delete(7)
        self.assertEqual(self.tree.root.right.key, 10)


if __name__ == "__main__":
    unittest.main()
