import unittest
from task_1 import  StringManipulator


class TestStringManipulator(unittest.TestCase):
    def setUp(self):
        self.sm = StringManipulator()

    def test_no_replacement(self):
        self.assertEqual(self.sm.replace_substring("hello", "x", "y"), "hello")

    def test_one_replacement(self):
        self.assertEqual(self.sm.replace_substring("hello", "l", "x"), "hexxo")

    def test_multiple_replacements(self):
        self.assertEqual(self.sm.replace_substring("hello", "ll", "x"), "hexo")

    def test_full_replacement(self):
        self.assertEqual(self.sm.replace_substring("aaa", "aaa", "b"), "b")

    def test_empty_string(self):
        self.assertEqual(self.sm.replace_substring("", "a", "b"), "")


if __name__ == '__main__':
    unittest.main()
