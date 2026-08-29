# 115. Distinct Subsequences
# Neetcode 150 (Important)
# Given two strings s and t, return the number of distinct subsequences of s which equals t.

# The test cases are generated so that the answer fits on a 32-bit signed integer.

# Example 1:

# Input: s = "rabbbit", t = "rabbit"
# Output: 3
# Explanation:
# As shown below, there are 3 ways you can generate "rabbit" from s.
# rabbbit
# rabbbit
# rabbbit

# Example 2:

# Input: s = "babgbag", t = "bag"
# Output: 5
# Explanation:
# As shown below, there are 5 ways you can generate "bag" from s.
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
 

# Constraints:

# 1 <= s.length, t.length <= 1000
# s and t consist of English letters.

# Recursive solution with memoization
# time complexity O(M*N) where M and N are the lengths of s and t respectively as we are exploring all combinations of s and t and memoizing the results to avoid redundant calculations.
# space complexity O(M*N) for the memoization dictionary that stores results for each combination of

# The below solution throws memory limit exceeded error as we used string as one of the pair in the dictionary
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def solve(st, i):
            if len(st)==len(t) and st==t: # if the current subsequence is equal to t then we found one valid subsequence and we return 1
                return 1
            if i>=len(s):
                return 0
            key = (st, i)
            if key in memo:
                return memo[key]
            # take
            take = solve(st+s[i], i+1)
            # leave
            leave = solve(st, i+1)
            memo[key] = take+leave
            return memo[key]
        return solve("", 0)
    
# Optimized solution using indices instead of strings in the memoization dictionary
# time complexity O(M*N) where M and N are the lengths of s and t respectively as we are exploring all combinations of s and t and memoizing the results to avoid redundant calculations.
# space complexity O(M*N) for the memoization dictionary that stores results for each combination of

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        memo = {}
        def solve(i, j):
            if j>=len(t): # if we have reached the end of t then we found one valid subsequence and we return 1
                return 1
            if i>=len(s): # if we have reached the end of s and we haven't found a valid subsequence then we return 0
                return 0
            key = (i, j)
            if key in memo:
                return memo[key]
            # found that character are equal and we take
            take = 0
            if s[i]==t[j]:
                take = solve(i+1, j+1)

            # if characters are unqual or if they are equal and we choose to skip
            leave = solve(i+1, j)

            memo[key] = take+leave
            return memo[key]
        return solve(0, 0)