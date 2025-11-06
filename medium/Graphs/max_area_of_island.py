# 695. Max Area of Island
# Neetcode 150

# You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

# Example 1:

# https://assets.leetcode.com/uploads/2021/05/01/maxarea1-grid.jpg
# Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
# Output: 6
# Explanation: The answer is not 11, because the island must be connected 4-directionally.

# Example 2:

# Input: grid = [[0,0,0,0,0,0,0,0]]
# Output: 0
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 50
# grid[i][j] is either 0 or 1.

from typing import List
from collections import deque

# Using DFS:
# time complexity O(M*N)
# space complexity O(M*N) in worst case when grid is filled with 1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            if i<0 or j<0 or i>=m or j>=n or grid[i][j]==0:
                return 0
            if grid[i][j]==-1:
                return 0
            grid[i][j]=-1
            left = right = top = bottom = 0 # to store area in 4 directions
            right += dfs(grid, i+1, j) # move right and add area of that direction
            left += dfs(grid, i-1, j)
            top += dfs(grid, i, j-1)
            bottom += dfs(grid, i, j+1)
            return 1+top+left+right+bottom # we do +1 to include current cell, the actual calculations happen in the return statements of 4 directions
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    area = dfs(grid, i, j)
                    max_area = max(max_area, area)
        return max_area

# Using BFS:
# time complexity O(M*N)
# space complexity O(M*N) for the queue in worst case when grid is filled with 1

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        m = len(grid)
        n = len(grid[0])
        self.q = deque()

        def bfs(grid):
            area = 1 # area is 1 because we have already added the first cell before calling bfs
            m = len(grid)
            n = len(grid[0])
            directions = [(1,0), (0,1), (-1,0), (0,-1)]
            while self.q:
                i, j = self.q.popleft()
                for d in directions:
                    ni = i+d[0]
                    nj = j+d[1]
                    if ni<0 or nj<0 or ni>=m or nj>=n or grid[ni][nj]==0:
                        continue
                    if grid[ni][nj]==-1:
                        continue
                    area+=1 # increment area for each valid land cell
                    grid[ni][nj]=-1
                    self.q.append((ni,nj))
            return area
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    self.q.append((i,j))
                    grid[i][j]=-1
                    area = bfs(grid)
                    max_area = max(max_area, area)
        return max_area
