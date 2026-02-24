# 678. Valid Parenthesis String
# Neetcode 150 (Important)

# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "(*)"
# Output: true

# Example 3:

# Input: s = "(*))"
# Output: true
 
# Constraints:

# 1 <= s.length <= 100
# s[i] is '(', ')' or '*'.


# brute force solution using DP + Memoization
# time complexity O(N^2) where N is the length of the string, we are iterating through the string and for each character we are iterating through the string again to find the last occurrence of that character
# space complexity O(N^2) for the memoization table to store the results of sub
class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = {}
        def solve(i, bal): # here balance keeps a count of open brackets '(' in the stack
            if bal<0: # if balance is negative, it means we have more closing brackets ')' than opening brackets '(', which is invalid, so we
                return False
            if i>=len(s):
                if bal==0:
                    return True
                else:
                    return False
            key = (i, bal)
            if key in memo:
                return memo[key]

            if s[i]=="(":
                memo[key] = solve(i+1, bal+1)
                return memo[key]
            if s[i]==")":
                memo[key] = solve(i+1, bal-1)
                return memo[key]
            star_open = solve(i+1, bal+1) # if the current character is '*', we can treat it as an opening bracket '(', so we increase the balance by 1
            star_close = solve(i+1, bal-1) # if the current character is '*', we can treat it as a closing bracket ')', so we decrease the balance by 1
            star_empty = solve(i+1, bal) # if the current character is '*', we can treat it as an empty string "", so we keep the balance unchanged
            memo[key] = star_open or star_close or star_empty
            return memo[key]
        return solve(0, 0)

 
# Solution using DP + Tabulation
# time complexity O(N^2) where N is the length of the string, we are iterating through the string and for each character we are iterating through the string again to find the last occurrence of that character
# space complexity O(N^2) for the dp table to store the results of subproblems

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False]*(n+2) for _ in range(n+1)] # here we take n+2 columns to avoid index out of range error when we try to access dp[i+1][bal+1] or dp[i+1][bal-1]
        # state definition
        # dp[i][j] = i to n-1, having seen j open brackets --> True, False
        # base case: s="", open = 0, should return true
        dp[n][0] = True
        for i in range(n-1, -1, -1):
            for bal in range(0, n+1):
                isValid = False
                if s[i]=="*":
                    ops = dp[i+1][bal+1]
                    close = False
                    if bal>0:
                        close = dp[i+1][bal-1]
                    empty = dp[i+1][bal]
                    isValid = isValid or ops or close or empty
                elif s[i]=='(':
                    isValid = isValid or dp[i+1][bal+1]
                elif bal>0:
                    isValid = isValid or dp[i+1][bal-1]
                dp[i][bal] = isValid
        return dp[0][0] # the result will be stored in dp[0][0] which means from index 0 to n-1, having seen 0 open brackets, is it valid or not
    
# Greedy approach using Stack
# time complexity O(N) where N is the length of the string, we are iterating through the string once
# space complexity O(N) in worst case when all characters in the string are '(', we are using a stack to store the indices of the open brackets and asterisk characters

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        open_stack = []
        asterisk_stack = []
        for i in range(n):
            if s[i]=='(':
                open_stack.append(i)
            elif s[i]=="*":
                asterisk_stack.append(i)
            else: # s[i]==')'
                if open_stack:
                    open_stack.pop()
                elif asterisk_stack: # asterisk acting as open bracket
                    asterisk_stack.pop()
                else:
                    return False
        # example : "*(())(*"
        # considering if there is an open bracket left in open_stack and star left asterisk_stack
        # and we need a close bracket
        while open_stack and asterisk_stack:
            if open_stack[-1]>asterisk_stack[-1]:
                return False
            open_stack.pop() # if there is an open bracket left in open_stack and star left asterisk_stack, we can use the asterisk as a close bracket to match the open bracket, so we pop from both stacks
            asterisk_stack.pop()
        return len(open_stack)==0
            
        
# Using trick of counting the number of open brackets and asterisk characters
# time complexity O(N) where N is the length of the string
# space complexity O(1)

class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        opn = 0
        close = 0
        for i in range(n):
            # left to right
            if s[i]=='(' or s[i]=="*":
                opn+=1
            else:
                opn-=1
            if opn<0:
                return False

        # right to left
        for i in range(n-1, -1, -1):
            
            if s[i]==')' or s[i]=="*":
                close+=1
            else:
                close-=1
            if close<0:
                return False
        return True
           
# Logic: we traverse the strings left to right and keep count of open brackets and consider asterisks as open brackets, 
# if at any point the count of open brackets becomes negative, it means we have more closing brackets than opening brackets, which is invalid, so we return false. 
# Then we traverse the string from right to left and keep count of closing brackets and consider asterisks as closing brackets, 
# if at any point the count of closing brackets becomes negative, it means we have more opening brackets than closing brackets, which is invalid, so we return false.