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
