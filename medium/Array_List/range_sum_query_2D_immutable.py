# 304. Range Sum Query 2D - Immutable

# Given a 2D matrix matrix, handle multiple queries of the following type:

# Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# Implement the NumMatrix class:

# NumMatrix(int[][] matrix) Initializes the object with the integer matrix matrix.
# int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
# You must design an algorithm where sumRegion works on O(1) time complexity.

# Example 1:

# Input
# ["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
# [[[[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]], [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]]
# Output
# [null, 8, 11, 12]

# Explanation
# NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
# numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
# numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
# numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 200
# -104 <= matrix[i][j] <= 104
# 0 <= row1 <= row2 < m
# 0 <= col1 <= col2 < n
# At most 104 calls will be made to sumRegion.

from typing import List

# time complexity: O(N^2) repeated everytime sumRegion is called
# space complexity: O(N^2)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(row1, row2+1):
            for j in range(col1, col2+1):
                s+=self.matrix[i][j]
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# time complexity: O(N^2) only once
# space complexity: O(N^2)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefix = [[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                # we are creating the prefix sum matrix where each cell is the sum of all the cells above and to the left of it, so we need to subtract the top left cell as it is added twice
                top = self.prefix[i-1][j] if i-1>=0 else 0 
                left = self.prefix[i][j-1] if j-1>=0 else 0
                topleft = self.prefix[i-1][j-1] if i-1>=0 and j-1>=0 else 0
                self.prefix[i][j] = matrix[i][j] + top + left - topleft                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # total is the sum of all the cells above and to the left of the bottom right cell, so we need to subtract the top and left cells as they are added twice, and add the top left cell as it is subtracted twice
        total = self.prefix[row2][col2] 
        top = self.prefix[row1-1][col2] if row1-1>=0 else 0
        left = self.prefix[row2][col1-1] if col1-1>=0 else 0
        topleft = self.prefix[row1-1][col1-1] if col1-1>=0 and row1-1>=0 else 0
        return total-top-left+topleft



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)