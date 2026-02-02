# 62. Unique Paths
# Neetcode 150 (Important)
# There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or equal to 2 * 109.

# Example 1:
# https://assets.leetcode.com/uploads/2018/10/22/robot_maze.png
# Input: m = 3, n = 7
# Output: 28

# Example 2:

# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
 

# Constraints:

# 1 <= m, n <= 100

# Recursive solution with memoization
# time complexity O(M*N) where M is number of rows and N is number of columns
# space complexity O(M+N-2) for recursion stack (depth of tree) + O(M*N) for memoization dictionary
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def solve(i, j):
            if i==m-1 and j==n-1: # base case reached bottom right corner
                return 1
            key = (i, j)
            if key in memo: # check if already computed
                return memo[key]
            right = 0
            down = 0
            if j<n:
                right = solve(i, j+1) # move right
            if i<m:
                down = solve(i+1, j) # move down
            memo[key] = right+down # add both ways
            return memo[key]
        return solve(0,0)
    
# Bottom-up dynamic programming solution
# time complexity O(M*N) where M is number of rows and N is number of columns
# space complexity O(M*N) for dp array

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        for i in range(m): # initialize first column, there is only one way to reach any cell in first column
            dp[i][0] = 1
        for j in range(n): # initialize first row, there is only one way to reach any cell in first row
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                # number of ways to reach current cell is sum of ways to reach cell above and cell to the left
                dp[i][j] = dp[i][j-1] + dp[i-1][j] 

        return dp[m-1][n-1] # return the value in bottom-right corner