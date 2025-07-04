# 150. Evaluate Reverse Polish Notation (NeetCode 150) Important

# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.
 
# Example 1:

# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9
# Example 2:

# Input: tokens = ["4","13","5","/","+"]
# Output: 6
# Explanation: (4 + (13 / 5)) = 6
# Example 3:

# Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# Output: 22
# Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
# = ((10 * (6 / (12 * -11))) + 17) + 5
# = ((10 * (6 / -132)) + 17) + 5
# = ((10 * 0) + 17) + 5
# = (0 + 17) + 5
# = 17 + 5
# = 22

# Constraints:

# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

from typing import List

# Time complexity: O(N), where N is the number of tokens.
# Space complexity: O(N), where N is the number of tokens in the stack.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for n in tokens:
            if n=='+':
                    stack.append(stack.pop()+stack.pop())
            elif n=='-': # in case of subtraction, the first popped element is subtracted from the second popped element (order matters here)
                d1 = stack.pop() 
                d2 = stack.pop()
                stack.append(d2-d1)
            elif n=='*':
                stack.append(stack.pop()*stack.pop())
            elif n=='/': # in case of division, the first popped element is divided by the second popped element (order matters here)
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a)) # # Use int() to truncate towards zero
            else:
                stack.append(int(n))
                
        return stack[0]