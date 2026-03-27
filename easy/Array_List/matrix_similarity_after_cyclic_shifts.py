# 2946. Matrix Similarity After Cyclic Shifts

# You are given an m x n integer matrix mat and an integer k. The matrix rows are 0-indexed.

# The following proccess happens k times:

# Even-indexed rows (0, 2, 4, ...) are cyclically shifted to the left.
# https://assets.leetcode.com/uploads/2024/05/19/lshift.jpg

# Odd-indexed rows (1, 3, 5, ...) are cyclically shifted to the right.
# https://assets.leetcode.com/uploads/2024/05/19/rshift-stlone.jpg

# Return true if the final modified matrix after k steps is identical to the original matrix, and false otherwise.

 

# Example 1:

# Input: mat = [[1,2,3],[4,5,6],[7,8,9]], k = 4

# Output: false

# Explanation:
# https://assets.leetcode.com/uploads/2024/05/19/t1-2.jpg
# In each step left shift is applied to rows 0 and 2 (even indices), and right shift to row 1 (odd index).



# Example 2:

# Input: mat = [[1,2,1,2],[5,5,5,5],[6,3,6,3]], k = 2

# Output: true

# Explanation:
# https://assets.leetcode.com/uploads/2024/05/19/t1-3.jpg


# Example 3:

# Input: mat = [[2,2],[2,2]], k = 3

# Output: true

# Explanation:
# As all the values are equal in the matrix, even after performing cyclic shifts the matrix will remain the same.

 

# Constraints:

# 1 <= mat.length <= 25
# 1 <= mat[i].length <= 25
# 1 <= mat[i][j] <= 25
# 1 <= k <= 50

from typing import List

# time complexity: O(M*N), space complexity: O(M*N)
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat)
        org = mat.copy()
        k = k % len(mat[0])
        for i in range(m):
            if i%2==0:
                mat[i] = mat[i][k:]+mat[i][:k]
            else:
                mat[i] = mat[i][-k:]+mat[i][:-k]
        return mat == org
    
    
class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m, n = len(mat), len(mat[0])
        k = k % n                          # mandatory normalisation for k>n

        for i in range(m):
            for j in range(n):
                if i % 2 == 0:             # even → left shift
                    if mat[i][j] != mat[i][(j + k) % n]: # instead of actually changing the position we just check the position change if the left shift is applied
                        return False
                else:                      # odd → right shift
                    if mat[i][j] != mat[i][(j - k) % n]: # instead of actually changing the position we just check the position change if the right shift is applied
                        return False
        return True