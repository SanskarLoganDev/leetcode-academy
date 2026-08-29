# 329. Longest Increasing Path in a Matrix
# Neetcode 150 (Important)
# Given an m x n integers matrix, return the length of the longest increasing path in matrix.

# From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

# Example 1:

# Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
# Output: 4
# Explanation: The longest increasing path is [1, 2, 6, 9].

# Example 2:

# Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
# Output: 4
# Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

# Example 3:

# Input: matrix = [[1]]
# Output: 1
 
# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# 0 <= matrix[i][j] <= 231 - 1


# Recursive DFS without memoization
from typing import List
# time complexity O(M*N*4^k) where k is the length of the longest increasing path and 4 as we have 4 directions to explore
# space complexity O(M*N)
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        # visited is not required as we only move when the next value is greater therefore previous value is always smaller and won't be considered.
        def dfs(i, j):
            best = 1
            for d in directions:
                ni = i+d[0]
                nj = j+d[1]
                
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>matrix[i][j]:
                    best = max(best, 1+dfs(ni, nj))
                
            return best
    
        max_len = 0
        for i in range(m):
            for j in range(n):
                res = dfs(i, j)
                max_len = max(res, max_len)

        return max_len

# Memoized DFS
# time complexity O(M*N)
# space complexity O(M*N)

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        memo = {} # here memo is intialized only once and not for every dfs call because we want to store the results of all cells
        # visited is not required as we only move when the next value is greater therefore previous value is always smaller and won't be considered.
        def dfs(i, j):
            key = (i, j)
            if key in memo:
                return memo[key]
            best = 1
            for d in directions:
                ni = i+d[0]
                nj = j+d[1]
                
                if 0<=ni<m and 0<=nj<n and matrix[ni][nj]>matrix[i][j]:
                    best = max(best, 1+dfs(ni, nj))
            memo[key] = best # we store here and not inside the directions for loop to store the final best value for this cell
            return memo[key]
    
        max_len = 0
        for i in range(m):
            for j in range(n):
                res = dfs(i, j) # call dfs for each cell
                max_len = max(res, max_len) # update max_len if needed

        return max_len

# Logical difference from usual DFS problems:
# In usual DFS problems we usually return or return 0 when we reach a invalid case. But here we have taken poistive case directly (that is when i and j are in range and next value is greater) and calculated best only in that case. If we do decide to start with the inavalid cases inside for loop then we would have to use continue statements to skip the invalid cases.