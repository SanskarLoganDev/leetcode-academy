# 225. Implement Stack using Queues

# Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

# Implement the MyStack class:

# void push(int x) Pushes element x to the top of the stack.
# int pop() Removes the element on the top of the stack and returns it.
# int top() Returns the element on the top of the stack.
# boolean empty() Returns true if the stack is empty, false otherwise.
# Notes:

# You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
# Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

# Example 1:

# Input
# ["MyStack", "push", "push", "top", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 2, 2, false]

# Explanation
# MyStack myStack = new MyStack();
# myStack.push(1);
# myStack.push(2);
# myStack.top(); // return 2
# myStack.pop(); // return 2
# myStack.empty(); // return False

# Using list as a queue

class MyStack:

    def __init__(self):
        self.q = []

    def push(self, x: int) -> None: # O(N^2)
        self.q.append(x)
        for i in range(len(self.q)-1): # O(N) for the for loop
            self.q.append(self.q.pop(0)) # pop(0) is O(N)

    def pop(self) -> int: # O(N)
        return self.q.pop(0)

    def top(self) -> int: # O(1)
        return self.q[0]

    def empty(self) -> bool: # O(1)
        return len(self.q)==0

# Using deque as a queue
from collections import deque
class MyStack:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None: # O(N)
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q)==0

from collections import deque
class MyStack:

    def __init__(self): # space: O(N)
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None: # O(N)
        self.q2.append(x)
        while self.q1:
            self.q2.append(self.q1.popleft()) # q1 will be empty after everything is popped from it

        # empty q2 for the next element, and store in q1 -> swapping
        self.q1, self.q2 = self.q2, self.q1

    def pop(self) -> int:
        return self.q1.popleft()

    def top(self) -> int:
        return self.q1[0]

    def empty(self) -> bool:
        return len(self.q1)==0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# The below solution is wrong even if it runs because in a queue, you cannot pop and peek from the same direction you inserted in a queue

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

# from collections import deque
# class MyStack(object):
    
#     def __init__(self):
#         self.container = deque()

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.container.append(x)
        

#     def pop(self):
#         """
#         :rtype: int
#         """
#         return self.container.pop()
        

#     def top(self):
#         """
#         :rtype: int
#         """
#         return self.container[-1]
        

#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.container)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()