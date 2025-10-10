# 54. Spiral Matrix
# Neetcode 150 (Important)

# Given an m x n matrix, return all elements of the matrix in spiral order.

# Example 1:
# https://assets.leetcode.com/uploads/2020/11/13/spiral1.jpg
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]

# Example 2:
# https://assets.leetcode.com/uploads/2020/11/13/spiral.jpg
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

from typing import List

# time complexity: O(M*N) where M is the number of rows and N is the number of columns in the matrix
# space complexity: O(1) ignoring the space required for the output list
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = 0
        bottom = len(matrix)-1
        left = 0
        right = len(matrix[0])-1
        res = []
        while top<=bottom and left<=right:
            for i in range(left, right+1): # top remains constant
                res.append(matrix[top][i])
            top+=1

            for i in range(top, bottom+1): # right remains constant
                res.append(matrix[i][right])
            right-=1

            # right -> left on the current bottom row (if still valid)
            if top <= bottom:
                for i in range(right, left-1, -1): # bottom stays constant
                    res.append(matrix[bottom][i])
                bottom-=1

            # bottom -> top on the current left column (if still valid)
            if left <= right:
                for i in range(bottom, top-1, -1): # left stays constant
                    res.append(matrix[i][left])
                left+=1

        return res
