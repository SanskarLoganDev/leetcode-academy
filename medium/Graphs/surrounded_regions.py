# 130. Surrounded Regions
# Neetcode 150

# You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

# Connect: A cell is connected to adjacent cells horizontally or vertically.
# Region: To form a region connect every 'O' cell.
# Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and none of the region cells are on the edge of the board.
# To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

# Example 1:

# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]

# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

# Explanation:

# In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

# Example 2:

# Input: board = [["X"]]

# Output: [["X"]]

# Constraints:

# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from typing import List
from collections import deque

# time complexity O(M*N)
# space complexity O(M*N) for the queue in worst case
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m =len(board)
        n = len(board[0])
        
        def bfs(board, i, j):
            directions = [(1,0),(0,1),(-1,0),(0,-1)]
            q = deque()
            q.append((i,j))

            while q:
                i, j = q.popleft()
                for d in directions:
                    ni = i+d[0]
                    nj = j+d[1]
                    
                    if ni<0 or nj<0 or ni>=m or nj>=n:
                        continue
                    if board[ni][nj]=="M" or board[ni][nj]=="X": # already visited or is 'X'
                        continue
                    board[ni][nj]="M" # mark as visited
                    q.append((ni,nj))

        # We will only apply BFS on the border cells which are 'O's
        # top and bottom row
        for j in range(n):
            if board[0][j]=="O":
                board[0][j]="M"
                bfs(board, 0, j)
            if board[m-1][j]=="O":
                board[m-1][j]="M"
                bfs(board, m-1, j)

        # first col and last col
        for i in range(m):
            if board[i][0]=="O":
                board[i][0]="M"
                bfs(board, i, 0)
            if board[i][n-1]=="O":
                board[i][n-1]="M"
                bfs(board, i, n-1)

        for i in range(m):
            for j in range(n):
                if board[i][j]=="O": # these are the surrounded regions
                    board[i][j]="X"
                elif board[i][j]=="M": # these are the non-surrounded regions
                    board[i][j]="O"
