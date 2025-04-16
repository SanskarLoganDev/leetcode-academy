# 796. Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.

# A shift on s consists of moving the leftmost character of s to the rightmost position.

# For example, if s = "abcde", then it will be "bcdea" after one shift.

# Example 1:

# Input: s = "abcde", goal = "cdeab"
# Output: true
# Example 2:

# Input: s = "abcde", goal = "abced"
# Output: false
 

# Constraints:

# 1 <= s.length, goal.length <= 100
# s and goal consist of lowercase English letters.

#Time and space complexity are O(N)

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):
            return False
        for i in range(len(goal)):
            s = s[1:]+s[0]
            if s==goal:
                return True
        return False
    
# alternate solution (same complexity, just less lines of code):
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s)==len(goal) and goal in s+s