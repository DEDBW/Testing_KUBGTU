from abc import ABC, abstractmethod


class StackInterface(ABC):
    @abstractmethod
    def push(self, value):
        pass

    @abstractmethod
    def pop(self):
        pass

    @abstractmethod
    def peek(self):
        pass

    @abstractmethod
    def is_empty(self):
        pass


class DoublyLinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedListStack(StackInterface):
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = DoublyLinkedListNode(value)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.tail.value

    def is_empty(self):
        return self.tail is None
