# 131. Palindrome Partitioning
# Neetcode 150 (Important)

# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]

# Example 2:
# Input: s = "a"
# Output: [["a"]]
 

# Constraints:

# 1 <= s.length <= 16
# s contains only lowercase English letters.

# Time complexity: O(N * 2^N) where N is length of string s
# There are O(2^N) possible partitions of a string of length N. For each partition, we need to check if each substring is a palindrome, which takes O(N) time in the worst case. 
# Therefore, the overall time complexity is O(N * 2^N).

# Space complexity: O(N) for the recursion stack and temporary storage
from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        temp = []
        def isPalindrome(c):
            return c==c[::-1] # check if string is palindrome
        def backtrack(idx): # here idx is the starting index of the substring
            if idx==len(s): # if we have reached the end of the string
                res.append(temp.copy())
            
            for i in range(idx, len(s)): # iterate through the string, i is the ending index of the substring
                if isPalindrome(s[idx:i+1]): # check if substring is palindrome
                    temp.append(s[idx:i+1]) # choose
                    backtrack(i+1)
                    temp.pop()

        backtrack(0)

        return res