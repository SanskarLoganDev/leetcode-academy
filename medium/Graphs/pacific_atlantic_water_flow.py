# 417. Pacific Atlantic Water Flow
# Neetcode 150

# There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

# The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

# The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

# Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

# Example 1:
# https://assets.leetcode.com/uploads/2021/06/08/waterflow-grid.jpg
# Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
# Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
# Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
# [0,4]: [0,4] -> Pacific Ocean 
#        [0,4] -> Atlantic Ocean
# [1,3]: [1,3] -> [0,3] -> Pacific Ocean 
#        [1,3] -> [1,4] -> Atlantic Ocean
# [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean 
#        [1,4] -> Atlantic Ocean
# [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean 
#        [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
# [3,0]: [3,0] -> Pacific Ocean 
#        [3,0] -> [4,0] -> Atlantic Ocean
# [3,1]: [3,1] -> [3,0] -> Pacific Ocean 
#        [3,1] -> [4,1] -> Atlantic Ocean
# [4,0]: [4,0] -> Pacific Ocean 
#        [4,0] -> Atlantic Ocean
# Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

# Example 2:

# Input: heights = [[1]]
# Output: [[0,0]]
# Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.
 

# Constraints:

# m == heights.length
# n == heights[r].length
# 1 <= m, n <= 200
# 0 <= heights[r][c] <= 105

from typing import List
from collections import deque
# time complexity O((M*N)^2)
# space complexity O(M*N) for visited set and queue
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        
        def bfs(i, j): # time complexity O(M*N) as the queue can have at most M*N elements
            q = deque()
            q.append((i,j))
            p = False
            a = False
            visited = set()
            visited.add((i,j))
            
            while q:
                i, j = q.popleft()
                val = heights[i][j]
                
                for d in directions:
                    ni = i+d[0]
                    nj = j+d[1]
                    if ni<0 or nj<0:
                        p = True
                        continue
                    if ni>=m or nj>=n:
                        a = True
                        continue
                    if (ni, nj) in visited:
                        continue
                    if heights[ni][nj]<=val:
                        q.append((ni, nj))
                        visited.add((ni, nj))
            return a and p
        res = []
        for i in range(m): # time complexity O(M*N)
            for j in range(n):
                if bfs(i, j):
                    res.append([i,j])
        return res

# Optimised solution using BFS:
# time complexity O(M*N)
# space complexity O(M*N) for visited sets

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        res = []
        pacificVisited = [[False]*n for _ in range(m)] # to check which cells can come up to pacific
        atlanticVisited = [[False]*n for _ in range(m)] # to check which cells can come up to atlantic
        
        def bfs(heights, i, j, visited):
            q = deque()
            q.append((i,j))
            visited[i][j] = True
            while q:
                i, j = q.popleft()
                for d in directions:
                    ni = i+d[0]
                    nj = j+d[1]
            
                    if ni<0 or nj<0 or ni>=m or nj>=n:
                        continue
                    if visited[ni][nj] or heights[ni][nj] < heights[i][j]:
                        continue
                    visited[ni][nj]=True
                    q.append((ni, nj))
        
        # top row and bottom row
        # top row: Pacific connected already
        # bottom row: Atlantic connected already

        for j in range(n):
            bfs(heights, 0, j, float("-inf"), pacificVisited) # top row
            bfs(heights, m-1, j, float("-inf"), atlanticVisited) # bottom row

        # first col and last col
        # first col: Pacific connected already
        # last col: Atlantic connected already

        for i in range(m):
            bfs(heights, i, 0, float("-inf"), pacificVisited) # first col
            bfs(heights, i, n-1, float("-inf"), atlanticVisited) # last col

        for i in range(m):
            for j in range(n):
                if pacificVisited[i][j] and atlanticVisited[i][j]:
                    res.append([i,j])
        
        return res


# optimised solution using DFS:

# time complexity O(M*N)
# space complexity O(M*N) for visited sets

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])
        res = []
        pacificVisited = [[False]*n for _ in range(m)] # to check which cells can come up to pacific
        atlanticVisited = [[False]*n for _ in range(m)] # to check which cells can come up to atlantic
        
        def dfs(heights, i, j, prevCellVal, visited):
            if i<0 or j<0 or i>=m or j>=n: # out of bounds
                return
            if visited[i][j] or heights[i][j]<prevCellVal: # if already visited or current cell height is less than previous cell height, we return
                return
            visited[i][j]=True # mark visited
            dfs(heights, i+1, j, heights[i][j], visited) # could also use directions array
            dfs(heights, i, j+1, heights[i][j], visited)
            dfs(heights, i-1, j, heights[i][j], visited)
            dfs(heights, i, j-1, heights[i][j], visited)
        # top row and bottom row
        # top row: Pacific connected already
        # bottom row: Atlantic connected already

        for j in range(n):
            dfs(heights, 0, j, float("-inf"), pacificVisited) # top row
            dfs(heights, m-1, j, float("-inf"), atlanticVisited) # bottom row

        # first col and last col
        # first col : Pacific connected already
        # last col: Atlantic connected already

        for i in range(m):
            dfs(heights, i, 0, float("-inf"), pacificVisited) # first col
            dfs(heights, i, n-1, float("-inf"), atlanticVisited) # last col

        for i in range(m):
            for j in range(n):
                if pacificVisited[i][j] and atlanticVisited[i][j]: # if both pacific and atlantic can reach this cell
                    res.append([i,j])
        
        return res

