# 20. VALID PARENTHESIS (NeetCode 150) Important

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def isValid(s):
    bracket_relation = {'(':')','[':']','{':'}'}
    bracket_list = [] # stack
    for bracket in s:
        if bracket in bracket_relation.keys():
            bracket_list.append(bracket)
        elif bracket in bracket_relation.values():
            if not bracket_list:
                return False # checking if closing bracket found in string when stack is empty
            if bracket!= bracket_relation[bracket_list[-1]]:
                return False
            bracket_list.pop()
    if len(bracket_list)==0:
        return True
    else:
        return False

print(isValid("()}[]"))

# Shorter simpler solution with same complexities

class Solution:
    def isValid(self, s: str) -> bool:
        parent = {'}':'{',']':'[',')':'('}
        stack = []
        for i in range(len(s)):
            if s[i] in parent.values():
                stack.append(s[i])
            elif len(stack)!=0 and s[i] in parent and stack[-1]==parent[s[i]]:
                stack.pop()
            else:
                return False
        return len(stack)==0