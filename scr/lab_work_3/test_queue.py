import unittest

from queue_ import *


class TestQueue(unittest.TestCase):
    def setUp(self) -> None:
        self.queue = Queue()

    def test_init(self) -> None:
        self.assertEqual(self.queue.data, [])
        self.assertEqual(self.queue.size, 0)
        self.assertEqual(self.queue.max_size, 100)

    def test_push(self) -> None:
        for i in range(1, 5):
            self.queue.push(i * 10)
        self.assertEqual(self.queue.data, [10, 20, 30, 40])
        self.assertEqual(self.queue.size, 4)
        for i in range(96):
            self.queue.push(i)
        with self.assertRaises(IndexError, msg='Очередь переполнена.'):
            self.queue.push(100)

    def test_pop(self) -> None:
        with self.assertRaises(IndexError, msg='Очередь пуста.'):
            self.queue.pop()
        self.queue.push(4)
        self.queue.push(5)
        self.queue.pop()
        self.assertEqual(self.queue.data, [5])
        self.assertEqual(self.queue.size, 1)

    def test_put_first_in_last(self) -> None:
        tmp_queue = Queue()
        for i in range(5):
            self.queue.push(i * 2)
            tmp_queue. push(i * 3)
        put_first_in_last(self.queue, tmp_queue)
        self.assertEqual(self.queue.data, [0, 2, 4, 6, 8, 0])
        self.assertEqual(tmp_queue.data, [3, 6, 9, 12])

    def test_swap(self) -> None:
        for i in range(3, 6):
            self.queue.push(i)
        for i in range(3):
            self.queue.push(i * 3)
        self.assertEqual(self.queue.data, [3, 4, 5, 0, 3, 6])
        swap(self.queue)
        self.assertEqual(self.queue.data, [0, 4, 5, 3, 3, 6])


if __name__ == '__main__':
    unittest.main()
