import unittest

from linked_list import *


class MyTestClass():
    def __init__(self, number, grade):
        self.number = number
        self.grade = grade


class TestLinkedList(unittest.TestCase):
    def setUp(self) -> None:
        self.linked_list = LinkedList()

    def test_add(self) -> None:
        self.assertEqual(self.linked_list.head, None)
        self.linked_list.add(1)
        self.assertEqual(self.linked_list.head.next, None)
        self.assertEqual(self.linked_list.head.data, 1)

    def test_extend(self) -> None:
        elements = [0, 10]
        self.linked_list.extend(elements)
        self.assertEqual(self.linked_list.head.next.next, None)
        self.assertEqual(self.linked_list.head.data, 0)
        self.assertEqual(self.linked_list.head.next.data, 10)

    def test_sort(self) -> None:
        elements = [10, 5, 1, 4, 9, 2]
        self.linked_list.extend(elements)
        self.linked_list.sort()
        self.assertEqual(self.linked_list.head.data, 1)
        self.assertEqual(self.linked_list.head.next.data, 2)
        self.assertEqual(self.linked_list.head.next.next.data, 4)

    def test_search(self) -> None:
        class1 = MyTestClass(number=451, grade=5)
        class2 = MyTestClass(number=123, grade=3)
        class3 = MyTestClass(number=925, grade=4)
        classes = [class1, class2, class3]
        self.linked_list.extend(classes)
        self.assertEqual(self.linked_list.search(number=123).grade, 3)
        self.assertEqual(self.linked_list.search(grade=4).number, 925)


if __name__ == '__main__':
    unittest.main()
