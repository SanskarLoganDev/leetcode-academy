# 895. Maximum Frequency Stack
# Neetcode 250

# Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

# Implement the FreqStack class:

# FreqStack() constructs an empty frequency stack.
# void push(int val) pushes an integer val onto the top of the stack.
# int pop() removes and returns the most frequent element in the stack.
# If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

# Example 1:

# Input
# ["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
# [[], [5], [7], [5], [7], [4], [5], [], [], [], []]
# Output
# [null, null, null, null, null, null, null, 5, 7, 5, 4]

# Explanation
# FreqStack freqStack = new FreqStack();
# freqStack.push(5); // The stack is [5]
# freqStack.push(7); // The stack is [5,7]
# freqStack.push(5); // The stack is [5,7,5]
# freqStack.push(7); // The stack is [5,7,5,7]
# freqStack.push(4); // The stack is [5,7,5,7,4]
# freqStack.push(5); // The stack is [5,7,5,7,4,5]
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
# freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
# freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
# freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].
 

# Constraints:

# 0 <= val <= 109
# At most 2 * 104 calls will be made to push and pop.
# It is guaranteed that there will be at least one element in the stack before calling pop.

# Time complexity of each function: O(1)
# Space complexity: O(N)
class FreqStack:

    def __init__(self):
        self.count = {}
        self.stacks = {} # its a hashmap of stacks that stores values with a particular count. 
        # Ex: {1: [5,7,4], 2: [5,7], 3:[5]} here5 will appear in counts of 1, 2 and 3 as its count is 3 in the array
        self.maxCount = 0

    def push(self, val: int) -> None:
        valCnt = self.count.get(val, 0) + 1
        self.count[val] = valCnt
        if valCnt > self.maxCount:
            self.maxCount = valCnt
            self.stacks[self.maxCount] = [] # initiating a new stack for the new maxCount
        self.stacks[valCnt].append(val) # append the val to its count in stack

    def pop(self) -> int:
        res = self.stacks[self.maxCount].pop() # pop the latest element with the highest frequency
        if not self.stacks[self.maxCount]: # if there is no element left in the maxCount stack, then maxCount needs to be reduced
            self.maxCount-=1
        self.count[res]-=1
        return res


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()