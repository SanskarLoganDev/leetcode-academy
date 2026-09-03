# 1260. Shift 2D Grid

# Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

# In one shift operation:

# Element at grid[i][j] moves to grid[i][j + 1].
# Element at grid[i][n - 1] moves to grid[i + 1][0].
# Element at grid[m - 1][n - 1] moves to grid[0][0].
# Return the 2D grid after applying shift operation k times.


# Example 1:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
# Output: [[9,1,2],[3,4,5],[6,7,8]]

# Example 2:


# Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
# Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]

# Example 3:

# Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
# Output: [[1,2,3],[4,5,6],[7,8,9]]
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m <= 50
# 1 <= n <= 50
# -1000 <= grid[i][j] <= 1000
# 0 <= k <= 100

from typing import List
# time complexity: O(N)
# space complexity: O(N)

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        temp = []
        for i in range(m):
            for j in range(n):
                temp.append(grid[i][j])

        len_arr = len(temp)
        if k>len_arr:
            k=k%len_arr
            
        def reverse(arr, start, end):
            l = start
            r = end
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l+=1
                r-=1
            return arr
        
        reverse(temp, 0, len_arr-1)
        reverse(temp, 0, k-1)
        reverse(temp, k, len_arr-1)
        x = 0
        for i in range(m):
            for j in range(n):
                grid[i][j] = temp[x]
                x+=1
        return grid
    
# for optimised solution just think how will you determine i = 6 (7th element) in temp (2D grid to 1D array) is in what row and column.
# row = i/(cols in grid) = 6//3 = 2
# col = i%(cols in grid) = 6%3 = 0
# therefore at [2, 0] in grid

# time complexity: O(N)
# space complexity: O(1)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        if k>(m*n):
            k=k%(m*n)
        len_arr = m*n # length of array if we convert 2D grid to 1D array
        def reverse(matrix, start, end):
            l = start
            r = end
            while l<r:
                matrix[l//n][l%n], matrix[r//n][r%n] = matrix[r//n][r%n], matrix[l//n][l%n]
                l+=1
                r-=1
            return matrix
        
        reverse(grid, 0, len_arr-1)
        reverse(grid, 0, k-1)
        reverse(grid, k, len_arr-1)

        return grid
        
        