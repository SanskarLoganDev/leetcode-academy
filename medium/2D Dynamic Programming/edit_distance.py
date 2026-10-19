# 72. Edit Distance
# Neetcode 150 (Important)

# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character
 

# Example 1:

# Input: word1 = "horse", word2 = "ros"
# Output: 3
# Explanation: 
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')

# Example 2:

# Input: word1 = "intention", word2 = "execution"
# Output: 5
# Explanation: 
# intention -> inention (remove 't')
# inention -> enention (replace 'i' with 'e')
# enention -> exention (replace 'n' with 'x')
# exention -> exection (replace 'n' with 'c')
# exection -> execution (insert 'u')
 
# Constraints:

# 0 <= word1.length, word2.length <= 500
# word1 and word2 consist of lowercase English letters.


# Using recursion
# time complexity O(3^(M+N)) where M and N are the lengths of word1 and word2 respectively as we are exploring all combinations of insert, delete, and replace operations.
# space complexity O(M+N) for the recursion stack in the worst case when we are exploring all combinations of insert, delete, and replace operations.
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        def solve(i, j):
            if j==n2: # if we have reached the end of word2 then we need to delete all remaining characters in word1 to convert it to word2
                return n1-i

            if i==n1: # if we have reached the end of word1 then we need to insert all remaining characters in word2 to convert it to word1
                return n2-j

            if word1[i]==word2[j]: # if the characters are equal then we can move to the next character in both strings without any operation
                return solve(i+1, j+1)

            # insert
            insert = 1+solve(i, j+1)
            # delete
            delete = 1+solve(i+1, j)
            # replace
            replace = 1+solve(i+1, j+1)

            return min(insert, delete, replace)
        return solve(0, 0)
            
        
# Using recursion with memoization
# time complexity O(M*N) where M and N are the lengths of word1 and word2 respectively as we are exploring all combinations of insert, delete, and replace operations and memoizing the results to avoid redundant calculations.
# space complexity O(M*N) for the memoization dictionary that stores results for each combination of indices in word1 and word2, and O(M+N) for the recursion stack in the worst case when we are exploring all combinations of insert, delete, and replace operations.

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        memo = {}
        def solve(i, j):
            if j==n2:
                return n1-i

            if i==n1:
                return n2-j

            key = (i, j)
            if key in memo:
                return memo[key]

            if word1[i]==word2[j]:
                return solve(i+1, j+1)

            # insert
            insert = 1+solve(i, j+1) # in insert we do not move i as the matching element was inserted before i, and now the ith element needs to be matched again
            # delete
            delete = 1+solve(i+1, j)
            # replace
            replace = 1+solve(i+1, j+1)

            memo[key] = min(insert, delete, replace)
            return memo[key]
        return solve(0, 0)
            
            
# Same solution and complexities but in reverse considering lengths of string instead of index
# Easier approach to prepare the bottom up solution next (bottom up from the start of table)

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        memo = {}
        def solve(m, n):
            if n==0:
                return m
            if m==0:
                return n
            
            key = (m, n)
            if key in memo:
                return memo[key]

            if word1[m-1]==word2[n-1]:
                return solve(m-1, n-1)

            # insert
            insert = 1+solve(m, n-1)

            # delete
            delete = 1+solve(m-1, n)

            # replace
            replace = 1+solve(m-1, n-1)

            memo[key] = min(insert, delete, replace)
            return memo[key]
        return solve(n1, n2)

# Bottom up DP
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1 = len(word1)
        n2 = len(word2)
        dp = [[0]*(n2+1) for _ in range(n1+1)] # the condition when i==0 or j==0
        # dp[i][j] = min operations for making s1 of length i and s2 of length j equal
        for i in range(n1+1):
            for j in range(n2+1):
                if i==0 or j==0:
                    dp[i][j] = i+j

                elif word1[i-1]==word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]

                else:
                    # insert
                    insert = 1+dp[i][j-1]

                    # delete
                    delete = 1+dp[i-1][j]

                    # replace
                    replace = 1+dp[i-1][j-1]
                    dp[i][j] = min(insert, delete, replace)

        return dp[n1][n2]

            
# Bottom up DP with reduced space complexity: O(min(n1, n2))

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # make word2 the shorter string
        if len(word2) > len(word1):
            word1, word2 = word2, word1

        n1 = len(word1)
        n2 = len(word2)

        # Base row:
        # empty word1 -> prefixes of word2
        dp = [0] * (n2 + 1)

        for j in range(n2 + 1):
            dp[j] = j

        for i in range(1, n1 + 1):

            # old dp[0], which is the diagonal for j=1
            prev = dp[0]

            # converting word1[:i] -> empty string
            dp[0] = i

            for j in range(1, n2 + 1):

                # save old dp[j] before overwriting it
                temp = dp[j]

                if word1[i - 1] == word2[j - 1]:
                    dp[j] = prev

                else:
                    # dp[j-1] = LEFT = current row
                    insert = 1 + dp[j - 1]

                    # dp[j] = TOP = previous row
                    delete = 1 + dp[j]

                    # prev = DIAGONAL = previous row, previous column
                    replace = 1 + prev

                    dp[j] = min(insert, delete, replace)

                # old TOP becomes diagonal for next j
                prev = temp

        return dp[n2]
        