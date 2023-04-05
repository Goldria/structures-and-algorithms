import unittest

from string_ import *


class TestString(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_delete_spaces(self):
        self.assertEqual(delete_spaces(
            '134  . 2344 . 244.'), '134. 2344. 244.')
        self.assertEqual(delete_spaces(
            'lol    . hello how are  you . my name is   .'), 'lol. hello how are  you. my name is.')


if __name__ == '__main__':
    unittest.main()
