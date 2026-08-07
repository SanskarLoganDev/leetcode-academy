# 723. Candy Crush

# This question is about implementing a basic elimination algorithm for Candy Crush.

# Given an m x n integer array board representing the grid of candy where board[i][j] represents the type of candy. A value of board[i][j] == 0 represents that the cell is empty.

# The given board represents the state of the game following the player's move. Now, you need to restore the board to a stable state by crushing candies according to the following rules:

# If three or more candies of the same type are adjacent vertically or horizontally, crush them all at the same time - these positions become empty.
# After crushing all candies simultaneously, if an empty space on the board has candies on top of itself, then these candies will drop until they hit a candy or bottom at the same time. No new candies will drop outside the top boundary.
# After the above steps, there may exist more candies that can be crushed. If so, you need to repeat the above steps.
# If there does not exist more candies that can be crushed (i.e., the board is stable), then return the current board.
# You need to perform the above rules until the board becomes stable, then return the stable board.

# Example 1:

# Input: board = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]
# Output: [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[110,0,0,0,114],[210,0,0,0,214],[310,0,0,113,314],[410,0,0,213,414],[610,211,112,313,614],[710,311,412,613,714],[810,411,512,713,1014]]
# Example 2:

# Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
# Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
 

# Constraints:

# m == board.length
# n == board[i].length
# 3 <= m, n <= 50
# 1 <= board[i][j] <= 2000

from typing import List

# time complexity: Total: O(m·n) rounds × O(m·n) work per round = O((m·n)²)
# Space: O(m·n)

class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        m = len(board)
        n = len(board[0])
        while True: # repeat crush+drop cycles until board is stable: O(m·n)
            crush = [[False]*n for _ in range(m)] # marks cells to be crushed this round: Space: O(m·n)
            done = True
            # marking rows
            for i in range(m): # process each row independently: O(m·n)
                for j in range(2, n):
                    if board[i][j] != 0 and board[i][j] == board[i][j-1] == board[i][j-2]:
                        crush[i][j] = crush[i][j-1] = crush[i][j-2] = True
                        done = False
            # marking cols
            for j in range(n): # process each column independently: O(m·n)
                for i in range(2, m):
                    if board[i][j] != 0 and board[i][j] == board[i-1][j] == board[i-2][j]:
                        crush[i][j] = crush[i-1][j] = crush[i-2][j] = True
                        done = False
            
            if done: # we did not crush anything or no matches found this round -> board is stable, exit loop
                break

            # crushing and moving
            new_board = [[0]*n for _ in range(m)] # build a fresh board with gravity applied: Space: O(m·n)
            for j in range(n): # O(m·n)
                write = m-1 # pointer scanning the OLD board from the bottom, skipping crushed cells
                for i in range(m-1, -1, -1):
                    while write>=0 and crush[write][j]:
                        write-=1
                    if write < 0: # no more surviving candies left in this column
                        break
                    new_board[i][j] = board[write][j] # drop the next surviving candy into place
                    write-=1
            board = new_board
        return board
