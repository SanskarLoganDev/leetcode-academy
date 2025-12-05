# 994. Rotting Oranges
# Neetcode 150
# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:
# https://assets.leetcode.com/uploads/2019/02/16/oranges.png
# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4

# Example 2:
# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

# Example 3:
# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

# Here we use multi-source BFS starting from all rotten oranges simultaneously.

from typing import List
from collections import deque

# time complexity O(M*N)
# space complexity O(M*N) in worst case when all oranges are rotten
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        m = len(grid)
        n = len(grid[0])
        directions= [(0,1),(1,0),(-1,0),(0,-1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    q.append((i,j)) # add all rotten oranges to queue
        mins = 0
        while q: # standard bfs loop
            l = len(q)
            flag = False # to check if any fresh orange got rotten in this minute
            while l: # we will go through all elements of current layer
                i, j = q.popleft()
                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]

                    if ni<0 or nj<0 or ni>=m or nj>=n:
                        continue
                    if grid[ni][nj]!=1:
                        continue
                    flag = True # a fresh orange got rotten
                    grid[ni][nj]=2 # mark orange as rotten
                    q.append((ni,nj))
                l-=1
            if flag:
                mins+=1 # increment minutes only if any fresh orange got rotten in this layer

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    return -1
        return mins # we could also remove flag and return mins-1 here as we increment mins even in last layer when no fresh orange gets rotten 
        #(exception is when there are no fresh oranges at all initially, we'll have to handle that in the start)