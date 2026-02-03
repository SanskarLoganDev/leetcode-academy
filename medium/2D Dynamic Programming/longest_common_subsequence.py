# 1143. Longest Common Subsequence
# Neetcode 150 (Important)

# Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.

# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.

# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.

# Recursive solution
# Time complexity: O(2^(n1+n2)) where n1 and n2 are lengths of text1 and text2 respectively.
# Space complexity: O(n1+n2) for the recursion stack.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)

        def solve(i, j):
            if i>=n1 or j>=n2:
                return 0
            if text1[i]==text2[j]: # characters match
                return 1+solve(i+1, j+1) # move both pointers and add 1 to result

            take1 = solve(i+1, j) # move pointer of text1
            take2 = solve(i, j+1) # move pointer of text2
            return max(take1, take2) # return the maximum of both options

        return solve(0, 0)
    
# recursive solution with memoization
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1 = len(text1)
        n2 = len(text2)
        memo = {}
        def solve(i, j):
            if i>=n1 or j>=n2:
                return 0
            key = (i, j)
            if key in memo: # check if result is already computed
                return memo[key]
            if text1[i]==text2[j]:
                return 1+solve(i+1, j+1)

            take1 = solve(i+1, j)
            take2 = solve(i, j+1)
            memo[key] = max(take1, take2) # store result in memo
            return memo[key] # return result

        return solve(0, 0)