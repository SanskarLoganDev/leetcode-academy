# 73. Set Matrix Zeroes
# Neetcode 150 (Important)

# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

# You must do it in place.

# Example 1:
# https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]

# Example 2:
# https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

# Constraints:

# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
 
# Follow up:

# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

# time complexity: O(M*N) where M is the number of rows and N is the number of columns in the matrix
# space complexity: O(M+N) where M is the number of rows and N is the number of columns in the matrix

from typing import List
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        cellsi = []
        cellsj = []
        for i in range(0,m):
            for j in range(0, n):
                if matrix[i][j]==0:
                    cellsi.append(i)
                    cellsj.append(j)

        for i in range(0,m):
            for j in range(0, n):
                if i in cellsi or j in cellsj:
                    matrix[i][j]=0
        

        