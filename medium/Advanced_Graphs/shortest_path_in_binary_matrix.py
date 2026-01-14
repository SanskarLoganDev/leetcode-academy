# 1091. Shortest Path in Binary Matrix

# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
# The length of a clear path is the number of visited cells of this path.

# Example 1:
# https://assets.leetcode.com/uploads/2021/02/18/example1_1.png

# Input: grid = [[0,1],[1,0]]
# Output: 2

# Example 2:
# https://assets.leetcode.com/uploads/2021/02/18/example2_1.png

# Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
# Output: 4

# Example 3:

# Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
# Output: -1

# Constraints:

# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1

# BFS Approach
# Here we don't have to compare different distances of different paths as the fastest path will reach the grid end first and then we return.

# time complexity O(n^2) where n is the number of rows or columns in the grid
# space complexity O(n^2) due to queue usage in BFS

from collections import deque
from typing import List
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (1,0), (-1,0), (0,-1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        if grid[0][0]==1 or grid[n-1][n-1]==1: # if start or end is blocked
            return -1
        if len(grid) == 1: # checking for single cell grid
            return 1
        def bfs(i, j):
            length = 1 # length is already 1 to include the starting cell
            q = deque()
            q.append((i, j))
            grid[i][j]=1
            while q:
                for _ in range(len(q)): # process all nodes at current level
                    i, j = q.popleft()
                    for d in directions:
                        ni = i+d[0]
                        nj = j+d[1]

                        if ni<0 or nj<0 or ni>=n or nj>=n: # boundary check
                            continue

                        if ni==n-1 and nj==n-1:
                            return length+1 # we do length+1 here because we are returning upon reaching the destination cell and the destination cell needs to be counted in the path length

                        if grid[ni][nj]!=0: # if cell is blocked or already visited
                            continue

                        grid[ni][nj] = 1 # mark visited
                        q.append((ni, nj))
                length+=1 # increase length after processing all nodes at current level
            return -1

        val = bfs(0,0)

        return val

# Dijkstra's Algorithm Approach with min-heap (could also be done using queue as all edge weights are same)
# time complexity O(n^2) where n is the number of rows or columns in the grid
# space complexity O(n^2) due to result array and min-heap usage
import heapq
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(0,1), (1,0), (-1,0), (0,-1), (-1, 1), (1, -1), (1, 1), (-1, -1)]
        if grid[0][0]!=0 or grid[n-1][n-1]!=0:
            return -1
        if len(grid)==1:
            return 1
        result = [[float("inf")]*n for _ in range(n)]
        min_heap = []
        result[0][0] = 0
        heapq.heappush(min_heap, (0,0,0)) # dist, i, j
        while min_heap:
            dist, i, j = heapq.heappop(min_heap)
            if i==n-1 and j==n-1:
                return dist+1 # we do +1 here because we are returning upon reaching the destination cell and the destination cell needs to be counted in the path length
            for d in directions:
                ni = i+d[0]
                nj = j+d[1]
                if ni<0 or nj<0 or ni>=n or nj>=n:
                    continue

                if grid[ni][nj]!=0:
                    continue
                grid[ni][nj]=1 # mark visited. Not much use here as we are using result array to track distances and repeated visits to a cell will only increse the distance and thus won't be considered anyways
                if dist+1< result[ni][nj]: # we do +1 here because each edge length is same = 1
                    heapq.heappush(min_heap, (dist+1, ni, nj))
                    result[ni][nj] = dist+1

        return -1 # if we exhaust all options and don't reach the end
