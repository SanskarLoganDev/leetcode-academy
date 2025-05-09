# 118. Pascal's Triangle  [Important Basic]

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
from typing import List

# Time complexity O(N^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp=[]
        n = numRows
        for i in range(n):
            row=[0]*(i+1)
            row[0]=1
            row[-1] = 1
            for j in range(1,i):
                row[j] = dp[i-1][j-1]+dp[i-1][j]
            dp.append(row)
        return dp