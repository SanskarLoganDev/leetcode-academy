# 1422. Maximum Score After Splitting a String

# Given a string s of zeros and ones, return the maximum score after splitting the string into two non-empty substrings (i.e. left substring and right substring).

# The score after splitting a string is the number of zeros in the left substring plus the number of ones in the right substring.

# Example 1:

# Input: s = "011101"
# Output: 5 
# Explanation: 
# All possible ways of splitting s into two non-empty substrings are:
# left = "0" and right = "11101", score = 1 + 4 = 5 
# left = "01" and right = "1101", score = 1 + 3 = 4 
# left = "011" and right = "101", score = 1 + 2 = 3 
# left = "0111" and right = "01", score = 1 + 1 = 2 
# left = "01110" and right = "1", score = 2 + 1 = 3
# Example 2:

# Input: s = "00111"
# Output: 5
# Explanation: When left = "00" and right = "111", we get the maximum score = 2 + 3 = 5
# Example 3:

# Input: s = "1111"
# Output: 3

# My solution complexity is O(n^2) and it is not optimal, but it works for the given problem. O(n) for iterating and O(n) for counting zeros and ones in the substrings.


class Solution:
    def maxScore(self, s: str) -> int:
        l = 1
        max_score = 0
        while l<=len(s)-1:
            left = s[0:l]
            right = s[l:len(s)]
            max_score = max(max_score, left.count("0")+right.count("1"))
            l+=1
        return max_score
    
    
# Optimal solution with O(n) complexity
class Solution:
    def maxScore(self, s: str) -> int:
        max_score = 0
        left_zeroes = 0
        left_ones = 0
        total_ones = s.count("1")
        for i in range(len(s)-1):
            if s[i]=="1": # s[i] is the last character of the left substring (acts as a split point)
                left_ones+=1
            else:
                left_zeroes+=1
            max_score = max(max_score, left_zeroes+total_ones-left_ones)
        return max_score