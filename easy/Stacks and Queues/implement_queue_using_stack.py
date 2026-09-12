# 232. Implement Queue using Stacks
# Neetcode 250

# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

# Implement the MyQueue class:

# void push(int x) Pushes element x to the back of the queue.
# int pop() Removes the element from the front of the queue and returns it.
# int peek() Returns the element at the front of the queue.
# boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

# Example 1:

# Input
# ["MyQueue", "push", "push", "peek", "pop", "empty"]
# [[], [1], [2], [], [], []]
# Output
# [null, null, null, 1, 1, false]

# Explanation
# MyQueue myQueue = new MyQueue();
# myQueue.push(1); // queue is: [1]
# myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
# myQueue.peek(); // return 1
# myQueue.pop(); // return 1, queue is [2]
# myQueue.empty(); // return false
 

# Constraints:

# 1 <= x <= 9
# At most 100 calls will be made to push, pop, peek, and empty.
# All the calls to pop and peek are valid.
 

# Follow-up: Can you implement the queue such that each operation is amortized O(1) time complexity? In other words, performing n operations will take overall O(n) time even if one of those operations may take longer.

# You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
# Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.

# Solution using 2 stacks
class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def push(self, x: int) -> None:
        self.input_stack.append(x) # O(1)

    def pop(self) -> int: # Amortized O(1)
        if len(self.output_stack)!=0: # most of the times this is triggered: O(1)
            return self.output_stack.pop() 
        else:
            while self.input_stack: # very few times this is triggered: O(N)
                self.output_stack.append(self.input_stack.pop())
            return self.output_stack.pop()

    def peek(self) -> int: # Amortized O(1)
        if len(self.output_stack)!=0: # most of the times this is triggered: O(1)
            return self.output_stack[-1]
        else:
            while self.input_stack: # very few times this is triggered: O(N)
                self.output_stack.append(self.input_stack.pop())
            return self.output_stack[-1]

    def empty(self) -> bool: # need to check both
        return len(self.input_stack)==0 and len(self.output_stack)==0

# Solution using 2 stacks, but a common function shuffle for shuffling
class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []

    def shuffle(self):
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def push(self, x: int) -> None:
        self.input_stack.append(x)

    def pop(self) -> int: # Amortized O(1)
        if len(self.output_stack)!=0:
            return self.output_stack.pop()
        else:
            self.shuffle()
            return self.output_stack.pop()

    def peek(self) -> int: # Amortized O(1)
        if len(self.output_stack)!=0:
            return self.output_stack[-1]
        else:
            self.shuffle()
            return self.output_stack[-1]

    def empty(self) -> bool:
        return len(self.input_stack)==0 and len(self.output_stack)==0

# Solution using 2 stacks and using variable
class MyQueue:

    def __init__(self):
        self.input_stack = []
        self.output_stack = []
        self.peekEl = -1

    def shuffle(self):
        while self.input_stack:
            self.output_stack.append(self.input_stack.pop())

    def push(self, x: int) -> None:
        if not self.input_stack:
            self.peekEl = x
        self.input_stack.append(x)

    def pop(self) -> int: # Amortized O(1)
        if len(self.output_stack)!=0:
            return self.output_stack.pop()
        else:
            self.shuffle()
            return self.output_stack.pop()

    def peek(self) -> int: # Always O(1) due to the peek variable maintained above
        if len(self.output_stack)!=0:
            return self.output_stack[-1]
        else:
            return self.peekEl

    def empty(self) -> bool:
        return len(self.input_stack)==0 and len(self.output_stack)==0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# The following code is wrong as the question does not allow pop from any other index, pop can only be done from the top
# class MyQueue:

#     def __init__(self):
#         self.stack = []

#     def push(self, x: int) -> None:
#         self.stack.append(x)

#     def pop(self) -> int:
#         return self.stack.pop(0)

#     def peek(self) -> int:
#         return self.stack[0]

#     def empty(self) -> bool:
#         return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# The following code is wrong as it does not follow the restrictions of only using stack to make a queue
# from collections import deque
# class MyQueue(object):

#     def __init__(self):
#         self.container = deque()

#     def push(self, x):
#         """
#         :type x: int
#         :rtype: None
#         """
#         self.container.appendleft(x)
        

#     def pop(self):
#         """
#         :rtype: int
#         """
#         return self.container.pop()

#     def peek(self):
#         """
#         :rtype: int
#         """
#         return self.container[-1]

#     def empty(self):
#         """
#         :rtype: bool
#         """
#         return len(self.container)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()