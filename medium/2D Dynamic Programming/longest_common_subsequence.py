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
# Time complexity: O(n1*n2) where n1 and n2 are lengths of text1 and text2 respectively.
# Space complexity: O(n1*n2) for the memoization
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
    
# Using bottom up dynamic programming (tabulation)
# Time complexity: O(n1*n2) where n1 and n2 are lengths of text1 and text2 respectively.
# Space complexity: O(n1*n2) for the dp table.

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]  # dp[i][j] will store the length of longest common subsequence of text1 of length i and text2 of length j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1]==text2[j-1]: # here we do i-1 and j-1 because dp is 1 indexed and text1 and text2 are 0 indexed
                    dp[i][j] = 1+dp[i-1][j-1] # if characters match, add 1 to the result from previous indices
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j]) # if characters do not match, take the maximum of skipping character from text1 or skipping character from text2

        return dp[m][n]
    
# Even more space optimised: O(min(m,n))

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1) # larger string
        n = len(text2)
        # make text2 the shorter string
        if n>m:
            text1, text2 = text2, text1
            m, n = n, m
        dp = [0]*(n+1)
        for i in range(1, m+1):
            prev = 0
            for j in range(1, n+1):
                temp = dp[j]
                if text1[i-1]==text2[j-1]:
                    dp[j] = 1 + prev
                else:
                    dp[j] = max(dp[j], dp[j-1])

                prev = temp

        return dp[n]
    
# Dry run: text1="abcde", text2="ace"
# m=5, n=3, text2 is already shorter so no swap
# dp=[0,0,0,0]
#
# Meaning before updating dp[j]:
# dp[j]   = TOP      = dp[i-1][j]
# dp[j-1] = LEFT     = dp[i][j-1]
# prev    = DIAGONAL = dp[i-1][j-1]
# temp saves old dp[j] before we overwrite it

# i=1, text1[i-1]='a'
# prev=0

# j=1, text2[j-1]='a'
# dp before=[0,0,0,0]
# temp=dp[1]=0                  # save TOP
# 'a'=='a' -> dp[1]=1+prev=1+0=1
# prev=temp=0
# dp=[0,1,0,0]

# j=2, text2[j-1]='c'
# temp=dp[2]=0                  # TOP=0
# 'a'!='c'
# dp[2]=max(dp[2],dp[1])=max(0,1)=1
#               TOP   LEFT
# prev=temp=0
# dp=[0,1,1,0]

# j=3, text2[j-1]='e'
# temp=dp[3]=0
# 'a'!='e'
# dp[3]=max(dp[3],dp[2])=max(0,1)=1
# prev=temp=0
# dp=[0,1,1,1]

# End row for 'a':
# dp=[0,1,1,1]
# Equivalent 2D row would mean:
# LCS("a","a")=1, LCS("a","ac")=1, LCS("a","ace")=1


# i=2, text1[i-1]='b'
# IMPORTANT: prev resets to 0 at start of every new row
# prev=0
# dp currently=[0,1,1,1] <- this is previous row

# j=1, compare 'b' and 'a'
# temp=dp[1]=1                  # save old TOP
# mismatch -> dp[1]=max(1,0)=1
# prev=temp=1
# dp=[0,1,1,1]

# j=2, compare 'b' and 'c'
# Here prev=1 because old dp[1] from previous row is now diagonal
# temp=dp[2]=1
# mismatch -> dp[2]=max(1,1)=1
# prev=temp=1
# dp=[0,1,1,1]

# j=3, compare 'b' and 'e'
# temp=dp[3]=1
# mismatch -> dp[3]=max(1,1)=1
# prev=temp=1
# dp=[0,1,1,1]

# End row for 'b':
# dp=[0,1,1,1]


# i=3, text1[i-1]='c'
# prev=0
# dp before=[0,1,1,1]

# j=1, compare 'c' and 'a'
# temp=dp[1]=1
# mismatch -> dp[1]=max(1,0)=1
# prev=temp=1
# dp=[0,1,1,1]

# j=2, compare 'c' and 'c'
# THIS IS IMPORTANT
# Before update:
# prev=1     -> DIAGONAL = old dp[i-1][j-1]
# dp[2]=1    -> TOP
# dp[1]=1    -> LEFT
# temp=dp[2]=1
# match -> dp[2]=1+prev=1+1=2
# prev=temp=1
# dp=[0,1,2,1]

# j=3, compare 'c' and 'e'
# temp=dp[3]=1                  # TOP=1
# dp[2]=2                       # LEFT=2, already updated this row
# mismatch -> dp[3]=max(1,2)=2
# prev=temp=1
# dp=[0,1,2,2]

# End row for 'c':
# dp=[0,1,2,2]


# i=4, text1[i-1]='d'
# prev=0
# dp before=[0,1,2,2]

# j=1, compare 'd' and 'a'
# temp=1
# mismatch -> dp[1]=max(1,0)=1
# prev=1
# dp=[0,1,2,2]

# j=2, compare 'd' and 'c'
# temp=2
# mismatch -> dp[2]=max(2,1)=2
# prev=2
# dp=[0,1,2,2]

# j=3, compare 'd' and 'e'
# temp=2
# mismatch -> dp[3]=max(2,2)=2
# prev=2
# dp=[0,1,2,2]

# End row for 'd':
# dp=[0,1,2,2]


# i=5, text1[i-1]='e'
# prev=0
# dp before=[0,1,2,2]

# j=1, compare 'e' and 'a'
# temp=1
# mismatch -> dp[1]=max(1,0)=1
# prev=1
# dp=[0,1,2,2]

# j=2, compare 'e' and 'c'
# temp=2
# mismatch -> dp[2]=max(2,1)=2
# prev=2
# dp=[0,1,2,2]

# j=3, compare 'e' and 'e'
# Before update:
# prev=2      -> DIAGONAL
# dp[3]=2     -> TOP
# dp[2]=2     -> LEFT
# temp=dp[3]=2
# match -> dp[3]=1+prev=1+2=3
# prev=temp=2
# dp=[0,1,2,3]

# Final dp=[0,1,2,3]
# return dp[n]=dp[3]=3
# LCS="ace", length=3