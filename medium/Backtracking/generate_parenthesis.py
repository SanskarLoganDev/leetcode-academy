# 22. Generate Parentheses  Important
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.


# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List

# Iterative solution

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []  # This list will store all valid combinations.
        # Each state is represented as a tuple: (current_string, count_open, count_close)
        stack = [("", 0, 0)]
        
        while stack:
            s, left, right = stack.pop()  # Get a state from the stack.
            
            # If the current string has used all 2*n characters, it's complete.
            if len(s) == 2 * n:
                res.append(s)
            else:
                # If we can add an opening parenthesis, do so.
                if left < n:
                    stack.append((s + "(", left + 1, right))
                # If we can add a closing parenthesis (only if it would remain valid),
                # then do so.
                if right < left:
                    stack.append((s + ")", left, right + 1))
        
        return res


# Recursive solution

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []  # This will store all valid combinations of parentheses.
        
        # backtrack is a helper function that builds the string s.
        # 'left' is the count of '(' used, 'right' is the count of ')' used.
        def backtrack(s, left, right):
            # If the current string s has length 2*n, we have used all parentheses.
            if len(s) == 2 * n:
                res.append(s)
                return
            
            # If we can add an opening parenthesis (we haven't used all n '('),
            # then add one and recursively build the rest of the string.
            if left < n:
                backtrack(s + "(", left + 1, right)
            
            # A closing parenthesis can be added only if there are more '(' than ')' in the current string.
            if right < left:
                backtrack(s + ")", left, right + 1)
        
        # Start with an empty string and no parentheses used.
        backtrack("", 0, 0)
        return res
