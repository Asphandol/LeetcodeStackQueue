from collections import deque

class MyQueue:
    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()
    def push(self, x):
        """
        A function to push an element x to the back of the queue.
        """
        while self.s1:
            self.s2.append(self.s1.pop())
        self.s1.append(x)
        while self.s2:
            self.s1.append(self.s2.pop())

    def pop(self):
        """
        Remove and return the element at the front of the queue.
        """
        return self.s1.pop()

    def peek(self):
        """
        Return the element at the front of the queue without removing it.
        """
        return self.s1[-1]

    def empty(self):
        """
        Check if the queue is empty.
        Returns True if the queue is empty, False otherwise.
        """
        return not self.s1
