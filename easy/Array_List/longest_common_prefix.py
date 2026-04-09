# 14. Longest Common Prefix
# Neetcode 250

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

# Simple logic: if we sort them then the most difference will be in the first and last elements as sort function sorts lexicographically
# time complexity: O(n * L * log(n) + L) which simplifies to O(n * L * log(n) where L is common subtring length
# space complexity: O(L)
from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        strs.sort()
        first = strs[0]
        last = strs[len(strs)-1]
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                break
            common+=first[i]
        return common

# using the same concept but using min max instead as they also evaluate lexicographically
# time complexity: O(n.L)
# space complexity: O(L)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = ""
        first = min(strs)
        last = max(strs)
        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                break
            common+=first[i]
        return common

