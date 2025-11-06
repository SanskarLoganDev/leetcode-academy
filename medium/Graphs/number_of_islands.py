# 200. Number of Islands
# Neetcode 150
# very similar to 463. Island Perimeter

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]

# Output: 1

# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]

# Output: 3

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

# Using DFS:
# time complexity O(M*N)
# space complexity O(M*N) in worst case when grid is filled with 1

from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        def dfs(grid, i, j):
            m = len(grid)
            n = len(grid[0])
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]=="0":
                return
            if grid[i][j]=="-1":
                return
            grid[i][j]="-1" # mark as visited
            dfs(grid, i+1, j)
            dfs(grid, i, j+1)
            dfs(grid, i-1, j)
            dfs(grid, i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    dfs(grid, i, j) # call dfs
                    islands+=1 # increment island count
        return islands

# Using BFS:
# time complexity O(M*N)
# space complexity O(M*N) for the queue in worst case when grid is filled with 1

from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0
        self.q = deque() # queue for bfs, we used self to access it in bfs function
        def bfs(grid): # bfs function, i and j are not needed as we will get them from the queue
            m = len(grid)
            n = len(grid[0])
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            while self.q:
                i, j = self.q.popleft()
                for d in directions:
                    ni = i+d[0]
                    nj = j+d[1]
                    if ni<0 or nj<0 or ni>=m or nj>=n or grid[ni][nj]=="0":
                        continue
                    if grid[ni][nj]=="-1":
                        continue
                    grid[ni][nj]="-1" # mark as visited
                    self.q.append((ni, nj))

        # loop through the grid to find islands
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="1":
                    self.q.append((i, j))  # add the first land cell to the queue
                    grid[i][j]="-1" # mark as visited for thr first land cell
                    bfs(grid)
                    islands+=1
        return islands
