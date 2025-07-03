# 36. Valid Sudoku  (Neetcode 150) Important

# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

# Example 1:

# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Example 2:

# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
 
# Constraints:

# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# Both solutions have time complexity of O(N^2) and space complexity of O(N), where N is the number of cells in the Sudoku board (which is 81 for a standard 9x9 board).

from typing import List
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_set = [set() for _ in range(9)]
        col_set = [set() for _ in range(9)]
        box_set = [set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                box_index = (r//3)*3 + (c//3) # Calculate the box index using integer division, here (r//3)*3 gives the starting row of the box and (c//3) gives the starting column of the box. We have  multiplied by 3 to get the correct box index.
                if (val in row_set[r] or val in col_set[c] or val in box_set[box_index]):
                    return False
                row_set[r].add(val)
                col_set[c].add(val)
                box_set[box_index].add(val)
        return True
    
# Explanation
# Think of the nine 3×3 boxes laid out in a 3×3 grid, numbered 0 through 8 in row-major order:

# [0] [1] [2]
# [3] [4] [5]
# [6] [7] [8]
# The expression r // 3 tells you which block-row you’re in (0, 1 or 2).

# The expression c // 3 tells you which block-column you’re in (0, 1 or 2).

# To turn that pair (block_row, block_col) into a single index in [0…8], you do:

# square_index = block_row * (number_of_block_columns) + block_col
# Since there are 3 blocks per row, number_of_block_columns is 3. Hence:

# square_index = (r // 3) * 3   +   (c // 3)
#              = block_row * 3  +   block_col
# You only multiply the block_row by 3 because you need to “skip over” that many whole rows of blocks. The block_col just offsets you within that row of blocks, so you add it directly—no extra factor of 3.

# Time complexities for all solutions are going to be constant O(1) since the board is always 9x9, which means we are always iterating through 81 cells.


# Brute Force Solution
class Solution:
    
    # Helper function to validate a 3x3 box
    def isValidBox(self, grid, sr, er, sc, ec):
        box_set = set()
        for row in range(sr, er+1):
            for col in range(sc, ec+1):
                if grid[row][col]=='.':
                    continue
                if grid[row][col] in box_set:
                    return False
                box_set.add(grid[row][col])
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # valididate rows

        for row in range(9):
            row_set = set()
            for col in range(9):
                if board[row][col]=='.':
                    continue
                if board[row][col] in row_set:
                    return False
                row_set.add(board[row][col])

        # validate columns

        for col in range(9):
            col_set = set()
            for row in range(9):
                if board[row][col]=='.':
                    continue
                if board[row][col] in col_set:
                    return False
                col_set.add(board[row][col])

        # validate boxes
        # sr = start row, er = end row, sc = start column, ec = end column
        # here we have +3 as the next start row is going to be 3 rows down and next start column is going to be 3 columns right.
        for sr in range(0,9,3):
            er = sr+2
            for sc in range(0,9,3):
                ec = sc+2
                if self.isValidBox(board, sr, er, sc, ec)!=True:
                    return False

        return True

# Smarter solution using just 1 set
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        string_set = set()

        for row in range(9):
            for col in range(9):
                if board[row][col]=='.':
                    continue
                
                # The following strings are constructed to check for duplicates in rows, columns, and boxes.
                string_row = f"{board[row][col]} found in row {row}"
                string_col = f"{board[row][col]} found in column {col}"
                string_box = f"{board[row][col]} found in box {row//3},{col//3}"

                if string_row in string_set or string_col in string_set or string_box in string_set:
                    return False
                string_set.add(string_row)
                string_set.add(string_col)
                string_set.add(string_box)

        return True

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row_set = set()
            col_set = set()
            box_set = set()
            for j in range(9):
                # Check the i-th row.
                if board[i][j] != '.':
                    if board[i][j] in row_set:
                        return False
                    row_set.add(board[i][j])
                
                # Check the i-th column.
                if board[j][i] != '.':
                    if board[j][i] in col_set:
                        return False
                    col_set.add(board[j][i])
                
                # Calculate the indices for the corresponding 3x3 sub-box.
                # For the i-th sub-box:
                # The starting row is (i // 3) * 3 and starting col is (i % 3) * 3.
                # j then iterates over the 9 cells in that sub-box.
                row_index = 3 * (i // 3) + (j // 3)
                col_index = 3 * (i % 3) + (j % 3)
                if board[row_index][col_index] != '.':
                    if board[row_index][col_index] in box_set:
                        return False
                    box_set.add(board[row_index][col_index])
        
        return True