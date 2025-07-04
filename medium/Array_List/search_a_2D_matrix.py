# 74. Search a 2D Matrix (NEETCODE 150) Important

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:


# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

from typing import List

# time complexity O(m log n) (due to binary search in each row), space complexity O(1)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for row in matrix:
            l=0
            r=len(row)-1
            while l<=r:
                mid = (l+r)//2
                if row[mid]==target:
                    return True
                elif target<row[mid]:
                    r = mid-1
                else:
                    l = mid+1
        return False
    
    
 # Time complexity O(log(m * n)) due to binary search to find the the target row and the target element in that row, space complexity O(1)   
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        top = 0
        bot = len(matrix)-1
        while top<=bot:
            mid_row = (top+bot)//2
            if target>matrix[mid_row][-1]: #If target is greater than the last element of the mid_row, then we need to search in the lower rows
                top = mid_row+1
            elif target<matrix[mid_row][0]: #If target is less than the first element of the mid_row, then we need to search in the upper rows
                bot = mid_row-1
            else:
                break
        if not top<=bot:
            return False

        target_row = matrix[(top+bot)//2] # This is the row where the target could be present, since it is between the first and last elements of this row
        l, r= 0, len(matrix[0])-1
        while l<=r:
            mid = (l+r)//2
            if target_row[mid]==target:
                return True
            elif target<target_row[mid]:
                r = mid-1
            else:
                l = mid+1
        return False