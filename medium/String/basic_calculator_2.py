# 227. Basic Calculator II Important

# Given a string s which represents an expression, evaluate this expression and return its value. 

# The integer division should truncate toward zero.

# You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

# Example 1:

# Input: s = "3+2*2"
# Output: 7
# Example 2:

# Input: s = " 3/2 "
# Output: 1
# Example 3:

# Input: s = " 3+5 / 2 "
# Output: 5

class Solution:
    def calculate(self, s: str) -> int:
        curr, stack, oper = 0, [], "+"
        operations = {"+","-","*","/"}
        for i in range(len(s)):
            if s[i].isdigit():
                curr = curr*10+int(s[i])
            if s[i] in operations or i==len(s)-1:
                if oper == "+":     # operations happen according to previous operator and not according to currrent operator/char
                    stack.append(curr)
                elif oper == "-":
                    stack.append(-curr)
                elif oper == "*":
                    stack[-1]*= curr
                else:
                    stack[-1] = int(stack[-1]/curr)
                    
                curr = 0
                oper = s[i]
        return sum(stack)