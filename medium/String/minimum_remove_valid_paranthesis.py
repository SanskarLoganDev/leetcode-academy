# 1249. Minimum Remove to Make Valid Parentheses
# Medium
# Topics
# Companies
# Hint
# Given a string s of '(' , ')' and lowercase English characters.

# Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

# Formally, a parentheses string is valid if and only if:

# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid strings, or
# It can be written as (A), where A is a valid string.
 

# Example 1:

# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# Example 2:

# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# Example 3:

# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        stack = [] # here the stack will hold the indexes of the brackets
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                if stack:
                    stack.pop()
                else:
                    s[i]=''
        for i in stack: # for index of s in stack remove the open brackets if any
            s[i]=''
        return ''.join(s)
        
        
# Example:
# Input String:
# "lee(t(c)o)de)"
# This string contains an extra ')' at the end.
# Processing Steps:
# Initial List Conversion:

# s = ['l','e','e','(', 't', '(', 'c', ')', 'o', ')', 'd', 'e', ')']
# First Pass – Iterating Over Characters:

# Index 0 to 2:
# Characters 'l', 'e', 'e' are not parentheses; nothing changes.
# Index 3 (Character '('):
# Push index 3 onto stack.
# stack = [3]
# Index 4 (Character 't'):
# Not a parenthesis.
# Index 5 (Character '('):
# Push index 5 onto stack.
# stack = [3, 5]
# Index 6 (Character 'c'):
# Not a parenthesis.
# Index 7 (Character ')'):
# Since stack is not empty, pop the top (index 5).
# stack = [3]
# Index 8 (Character 'o'):
# Not a parenthesis.
# Index 9 (Character ')'):
# stack is not empty, pop the top (index 3).
# stack = []
# Index 10 (Character 'd'):
# Not a parenthesis.
# Index 11 (Character 'e'):
# Not a parenthesis.
# Index 12 (Character ')'):
# stack is empty, so mark this character for removal by setting s[12] = ''.
# After First Pass:

# The list s becomes:
# ['l','e','e','(', 't', '(', 'c', ')', 'o', ')', 'd','e', '']
# stack is empty (all unmatched '(' have been matched).
# Second Pass:

# Since stack is empty, there’s no additional removal.
# Join the List:

# ''.join(s) yields:
# "lee(t(c)o)de"
# This is the valid string with the minimum number of removals.