# 22. Generate Parentheses 
# Neetcode 150 (Important)

# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# Example 2:

# Input: n = 1
# Output: ["()"]

from typing import List

# Traditional backtracking solution
# time complexity: O(2^(2n) * 2n) where n is number of pairs of parentheses
# space complexity: O(2n) where n is number of pairs of parentheses (temp list can go upto 2n in worst case), also depth of recursion tree can go upto 2n

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def isValid(s): # helper function to check if parentheses string is valid (O(2n) time)
            count = 0
            for i in range(len(s)):
                if count<0:
                    return False
                if s[i]=="(":
                    count+=1
                else:
                    count-=1
            return count==0
        def backtrack(): # backtracking function O(2^(2n)) calls
            if len(temp)==2*n: # base case where we have used all parentheses
                if isValid(temp):
                    key = "".join(temp.copy()) # convert list to string
                    res.append(key) # add to results
                return
            temp.append("(") # Adding the "(" parenthesis
            backtrack()
            temp.pop() # backtrack

            temp.append(")") # Adding the ")" parenthesis
            backtrack()
            temp.pop()

        backtrack()
        return res

# Optimized backtracking solution
# time complexity: O(2^(2n)) where n is number of pairs of parentheses
# time complexity if we consider catalan number: O(4^n/sqrt(n))
# space complexity: O(2n) where n is number of pairs of parentheses (temp list can go upto 2n in worst case), also depth of recursion tree can go upto 2n

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def backtrack(opes, close):
            if len(temp)==2*n:
                key = "".join(temp.copy()) # convert list to string
                res.append(key)
                return
            if opes<n: # we can add opening parenthesis if we have not used all n opening parentheses
                temp.append("(") # add opening parenthesis
                backtrack(opes+1, close)
                temp.pop()

            if close<opes: # we can add closing parenthesis only if there are more opening parentheses used
                temp.append(")")
                backtrack(opes, close+1)
                temp.pop()

        backtrack(0,0)
        return res


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
