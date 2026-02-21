# 155. Min Stack (Neetcode 150) Important
# Neetcode 150 (Important)

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

# Example 1:

# Input
# ["MinStack","push","push","push","getMin","pop","top","getMin"]
# [[],[-2],[0],[-3],[],[],[],[]]

# Output
# [null,null,null,null,-3,null,0,-2]

# Explanation
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin(); // return -3
# minStack.pop();
# minStack.top();    // return 0
# minStack.getMin(); // return -2
 
# Constraints:

# -231 <= val <= 231 - 1
# Methods pop, top and getMin operations will always be called on non-empty stacks.
# At most 3 * 104 calls will be made to push, pop, top, and getMin.


# Line to remember: # You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = [] # to keep track of the minimum element at each level of the stack

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val,self.minStack[-1])) # compare with the last minimum element
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop() # to maintain the minimum element stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


# Explanation of the approach:

# Think of `minStack` as **a “shadow stack” with the exact same height as `stack`**.

# * `stack[i]` stores the actual value at level `i`
# * `minStack[i]` stores **the minimum of `stack[0..i]`** (the minimum *up to that depth*)

# So when you `pop()` from the real stack, you must also `pop()` from the shadow stack to keep both stacks aligned at the same depth.

# If you *don’t* pop from `minStack`, its “top minimum” would still correspond to an element that no longer exists in `stack`.

# ---

# ## Example (your given sample)

# Operations:

# ### 1) push(-2)

# * stack: `[-2]`
# * minStack: `[-2]`  (min up to here is -2)

# ### 2) push(0)

# * stack: `[-2, 0]`
# * minStack: `[-2, -2]`  (min(-2,0) = -2)

# ### 3) push(-3)

# * stack: `[-2, 0, -3]`
# * minStack: `[-2, -2, -3]`  (min so far becomes -3)

# Now:

# * `getMin()` returns `minStack[-1] = -3` ✅

# ### 4) pop()

# We remove the top element from the real stack: `-3`

# If we pop both:

# * stack becomes `[-2, 0]`
# * minStack becomes `[-2, -2]`

# Now `getMin()` returns `-2` ✅ (correct, because -3 is gone)

# ---

# ## What if we *didn’t* pop from minStack?

# After popping from only `stack`:

# * stack: `[-2, 0]`
# * minStack: `[-2, -2, -3]`  ❌ (still thinks there are 3 levels)

# Now `getMin()` would still return `-3` ❌
# But `-3` isn’t even in the stack anymore.

# So you **must** pop from `minStack` to “rewind” the minimum back to what it was at the previous depth.

# ---

# ## Why you don’t “lose the minimum”

# You’re not storing *one* minimum value; you’re storing the minimum **at every level**.

# In the example, after pushing 0 you already stored `-2` again:

# * minStack was `[-2, -2]`

# So when you remove `-3`, the previous minimum (`-2`) is still right there on top after the pop.

# ---

# ## Another quick example with duplicates

# push(5), push(3), push(3)

# * stack: `[5, 3, 3]`
# * minStack: `[5, 3, 3]`

# pop() removes top 3:

# * stack: `[5, 3]`
# * minStack: `[5, 3]`
#   getMin() is still 3 ✅ (the earlier 3 remains)

# pop() again removes the other 3:

# * stack: `[5]`
# * minStack: `[5]`
#   getMin() becomes 5 ✅

# This is exactly why `minStack` tracks min **per level**, not globally.

# If you want, I can also show the invariant as a one-liner proof: `minStack[-1] == min(stack)` always holds because both stacks change together.
