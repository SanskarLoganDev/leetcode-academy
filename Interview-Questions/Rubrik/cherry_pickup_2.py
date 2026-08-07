# 1463. Cherry Pickup II

# You are given a rows x cols matrix grid representing a field of cherries where grid[i][j] represents the number of cherries that you can collect from the (i, j) cell.

# You have two robots that can collect cherries for you:

# Robot #1 is located at the top-left corner (0, 0), and
# Robot #2 is located at the top-right corner (0, cols - 1).
# Return the maximum number of cherries collection using both robots by following the rules below:

# From a cell (i, j), robots can move to cell (i + 1, j - 1), (i + 1, j), or (i + 1, j + 1).
# When any robot passes through a cell, It picks up all cherries, and the cell becomes an empty cell.
# When both robots stay in the same cell, only one takes the cherries.
# Both robots cannot move outside of the grid at any moment.
# Both robots should reach the bottom row in grid.

# Example 1:

# Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
# Output: 24
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
# Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
# Total of cherries: 12 + 12 = 24.

# Example 2:


# Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],[1,0,2,3,0,0,6]]
# Output: 28
# Explanation: Path of robot #1 and #2 are described in color green and blue respectively.
# Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
# Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
# Total of cherries: 17 + 11 = 28.
 

# Constraints:

# rows == grid.length
# cols == grid[i].length
# 2 <= rows, cols <= 70
# 0 <= grid[i][j] <= 100

from typing import List

# Time	O(9^m) exponential as we have 9 choices for each step: 3 * 3 choices for each robot
# Space: Max recursion depth = m (one call per row) → O(m)
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        def solve(row, c1, c2):
            # bound check for rows
            if row >= m:
                return 0 # no cherry outside bound

            if c1==c2: # same cell can be taken only once
                cherry_count = grid[row][c1]
            else:
                cherry_count = grid[row][c1] + grid[row][c2]
            
            ans = 0
            for i in range(-1,2):
                for j in range(-1,2):
                    newRow = row+1
                    newC1 = c1+i
                    newC2 = c2+j

                    # checking for bounds
                    if newC1 < 0 or newC1 >=n or newC2<0 or newC2 >= n:
                        continue

                    ans = max(ans, solve(newRow, newC1, newC2))

            return cherry_count + ans

        m = len(grid)
        n = len(grid[0])
        return solve(0, 0, n-1)
    
# optimsied solution using memoization

# time complexity: O(m*n^2)
# Explanation:
# Number of distinct states

# The memo key is (row, c1, c2):

# row ranges over m values
# c1 ranges over n values
# c2 ranges over n values

# Total distinct states = O(m × n²)

# Work per state

# Each state does O(9) work (the 3×3 nested loop for robot movements) — but crucially, only on the first call. 
# Every subsequent call with the same (row, c1, c2) hits the memo and returns in O(1).

# Space complexity: O(m)
# Just like before, the maximum depth of recursion is O(m) (one call per row, since row increases by 1 each time and the base case triggers at row >= m). 
# This contributes O(m) stack space.

# Bottom up approach
# dp[row][c1][c2] --> max cherries collected by R1 and R2 till (row, C1) -> R1 and (row, C2) -> R2