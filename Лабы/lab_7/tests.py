import unittest
from task_1 import DoublyLinkedListStack


class TestDoublyLinkedListStack(unittest.TestCase):

    def setUp(self):
        self.stack = DoublyLinkedListStack()

    def test_push_to_empty_stack(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

    def test_push_to_non_empty_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.peek(), 20)

    def test_pop_from_non_empty_stack(self):
        self.stack.push(10)
        self.stack.push(20)
        self.assertEqual(self.stack.pop(), 20)
        self.assertEqual(self.stack.peek(), 10)

    def test_pop_from_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.pop()

    def test_peek_from_empty_stack(self):
        with self.assertRaises(IndexError):
            self.stack.peek()

    def test_peek_from_non_empty_stack(self):
        self.stack.push(10)
        self.assertEqual(self.stack.peek(), 10)

    def test_is_empty_on_new_stack(self):
        self.assertTrue(self.stack.is_empty())

    def test_is_empty_after_push(self):
        self.stack.push(10)
        self.assertFalse(self.stack.is_empty())

    def test_is_empty_after_pop_all(self):
        self.stack.push(10)
        self.stack.pop()
        self.assertTrue(self.stack.is_empty())


if __name__ == '__main__':
    unittest.main()
