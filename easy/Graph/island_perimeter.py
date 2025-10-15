# 463. Island Perimeter

# You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

# Example 1:

# https://assets.leetcode.com/uploads/2018/10/12/island.png
# Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
# Output: 16
# Explanation: The perimeter is the 16 yellow stripes in the image above.

# Example 2:

# Input: grid = [[1]]
# Output: 4

# Example 3:

# Input: grid = [[1,0]]
# Output: 4
 

# Constraints:

# row == grid.length
# col == grid[i].length
# 1 <= row, col <= 100
# grid[i][j] is 0 or 1.
# There is exactly one island in grid.

# Solution using DFS:

from typing import List

# Best solution using simple traversal without dfs or bfs
# time complexity O(M*N)
# space complexity O(1)

from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        perimeter = 0
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    continue
                for d in directions:
                    ni = i + d[0]
                    nj = j + d[1]
                    if ni<0 or nj<0 or ni>=m or nj>=n or grid[ni][nj]==0:
                        perimeter+=1
        return perimeter

# time complexity O(M*N)
# Auxiliary space: O(1), Stack space complexity: O(M*N) in worst case when grid is filled with 1
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid) # length of column
        n = len(grid[0]) # length of row
        self.perimeter = 0 # to store the perimeter (global variable)

        def dfs(grid, i, j):
            m = len(grid) # length of column
            n = len(grid[0]) # length of row
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                self.perimeter+=1
                return
            if grid[i][j]==-1:
                return
            grid[i][j]=-1 # marked visited

            # the following calls will traverse in all 4 directions
            dfs(grid, i+1, j)
            dfs(grid, i-1, j)
            dfs(grid, i, j+1)
            dfs(grid, i, j-1)

        for i in range(m): # traverse the grid row
            for j in range(n): # traverse the grid column
                if grid[i][j]==1:
                    dfs(grid, i, j) # call the dfs function
                    return self.perimeter

# Solution using BFS:

# time complexity O(M*N)
# Space complexity: O(M*N) for queue data structure

from collections import deque
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid) # length of column
        n = len(grid[0]) # length of row
        perimeter = 0
        q = deque()
        directions = [[1,0], [-1,0], [0,1],[0,-1]] # to traverse in 4 directions
        for i in range(m):
            if q:
                break
            for j in range(n):
                if grid[i][j]==1:
                    q.append((i,j))
                    grid[i][j]=-1
                    break
        if not q: # if there is no land (edge case)
            return 0
        while q:
            i, j = q.popleft()
            # check the 4 neighbours: (i+1, j), (i-1, j), (i, j+1), (i, j-1), defined in directions array

            for d in directions:
                ni = i + d[0] # here we did not do i = i + d[0] because we need the original i, j values for other directions
                nj = j + d[1]
                if ni<0 or nj<0 or ni>=m or nj>=n or grid[ni][nj]==0:
                    perimeter+=1 # if it is out of bound or it is water, we increase the perimeter by 1
                    continue
                if grid[ni][nj]==-1: # already visited
                    continue
                else:
                    q.append((ni, nj)) # add to queue
                    grid[ni][nj]=-1 # mark visited
        return perimeter