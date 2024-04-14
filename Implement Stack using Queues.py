from collections import deque

class MyStack:

    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()

    def push(self, x: int) -> None:
        """
        A function to push an element x to the back of the stack.
        """
        self.queue1.append(x)

    def pop(self) -> int:
        """
        A function to remove and return the top element of the stack.
        """
        while len(self.queue1)>1:
            self.queue2.append(self.queue1.popleft())
        tmp = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return tmp

    def top(self) -> int:
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())
        
        top_element = self.queue1[0]
        
        self.queue2.append(self.queue1.popleft())
        
        # Swap q1 and q2
        self.queue1, self.queue2 = self.queue2, self.queue1
        
        return top_element

    def empty(self) -> bool:
        """
        Check if the stack is empty.
        Returns True if the stack is empty, False otherwise.
        """
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()