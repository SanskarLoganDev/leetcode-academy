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
            insert = 1+solve(i, j+1)
            # delete
            delete = 1+solve(i+1, j)
            # replace
            replace = 1+solve(i+1, j+1)

            memo[key] = min(insert, delete, replace)
            return memo[key]
        return solve(0, 0)
            
        