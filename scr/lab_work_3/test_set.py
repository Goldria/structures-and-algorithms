import unittest

from set_ import *


class TestSet(unittest.TestCase):
    def setUp(self) -> None:
        self.set = MySet()

    def test_init(self) -> None:
        self.assertEqual(self.set.data, [])

    def test_add(self) -> None:
        for i in range(5):
            self.set.add(i)
        self.assertEqual(self.set.data, [0, 1, 2, 3, 4])
        self.set.add(3)
        self.assertEqual(self.set.data, [0, 1, 2, 3, 4])

    def test_intersection(self) -> None:
        for i in range(4):
            self.set.add(i)
        new_set = MySet([4, 5])
        self.assertEqual(self.set.intersection(new_set).data, [])
        new_set = MySet([1, 2, 3, 4, 5])
        self.assertEqual(self.set.intersection(new_set).data, [1, 2, 3])
        new_set = MySet([0, 1, 2, 3])
        self.assertEqual(self.set.intersection(new_set).data, [0, 1, 2, 3])

    def test_difference(self) -> None:
        for i in range(4):
            self.set.add(i)
        new_set = MySet([4, 5])
        self.assertEqual(self.set.difference(new_set).data, [0, 1, 2, 3])
        new_set = MySet([1, 2, 3, 4, 5])
        self.assertEqual(self.set.difference(new_set).data, [0])
        new_set = MySet([0, 1, 2, 3])
        self.assertEqual(self.set.difference(new_set).data, [])

    def test_unoin(self) -> None:
        for i in range(4):
            self.set.add(i)
        new_set = MySet([4, 5])
        self.assertEqual(self.set.union(new_set).data, [0, 1, 2, 3, 4, 5])
        new_set = MySet([1, 2])
        self.assertEqual(self.set.union(new_set).data, [0, 1, 2, 3])
        new_set = MySet([10, 12])
        self.assertEqual(self.set.union(new_set).data, [0, 1, 2, 3, 10, 12])

    def test_copy(self) -> None:
        for i in range(4):
            self.set.add(i)
        new_set = self.set.copy()
        self.assertEqual(new_set.data, [0, 1, 2, 3])

    def test_find_available_toys(self) -> None:
        self.set = MySet([1, 2, 3, 4, 5]).copy()
        sets = [[], self.set.data, [2, 3, 4, 5], [3, 5, 7]]
        available_elems = find_available_toys(sets)
        self.assertEqual(available_elems.data, [3, 5])

    def test_find_missing_toys(self) -> None:
        self.set = MySet([1, 2, 3, 4, 5]).copy()
        sets = [[], self.set.data, [2, 3, 4, 5], [3, 5, 7]]
        elems = [0, 1, 2, 3, 4, 5, 6, 7]
        missing_elems = find_missing_toys(sets, elems)
        self.assertEqual(missing_elems.data, [0, 6])


if __name__ == '__main__':
    unittest.main()
