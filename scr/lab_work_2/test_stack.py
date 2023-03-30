import unittest

from stack import *


class TestStack(unittest.TestCase):
    def setUp(self) -> None:
        self.stack_ = Stack()

    def test_init(self) -> None:
        self.assertEqual(self.stack_.data, [])
        self.assertEqual(self.stack_.size, 0)

    def test_push(self) -> None:
        self.stack_.push(5)
        self.stack_.push(10)
        self.stack_.push(20)
        self.stack_.push(4)
        self.assertEqual(self.stack_.data, [5, 10, 20, 4])
        self.assertEqual(self.stack_.size, 4)

    def test_pop(self) -> None:
        with self.assertRaises(IndexError, msg='Стек пустой.'):
            self.stack_.pop()
        self.stack_.push(4)
        self.stack_.push(5)
        self.stack_.pop()
        self.assertEqual(self.stack_.data, [4])
        self.assertEqual(self.stack_.size, 1)

    def test_count_average(self) -> None:
        for i in range(5):
            self.stack_.push(i)
        self.assertEqual(count_average(self.stack_), 2)

    def test_delete_elements(self) -> None:
        for i in range(5):
            self.stack_.push(i)
        self.assertEqual(self.stack_.data, [0, 1, 2, 3, 4])
        self.assertEqual(self.stack_.size, 5)
        delete_elements(self.stack_)
        self.assertEqual(self.stack_.data, [3, 4])


if __name__ == '__main__':
    unittest.main()
