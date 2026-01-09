# 51. N-Queens
# Neetcode 150 (Important)

# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

# Example 1:
# https://assets.leetcode.com/uploads/2020/11/13/queens.jpg

# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

# Example 2:

# Input: n = 1
# Output: [["Q"]]
 
# Constraints:

# 1 <= n <= 9

from typing import List

# time complexity: O(N!) where N is the size of the board (n x n)
# explanation for time complexity:
# In the N-Queens problem, we need to place N queens on an N x N chessboard such that no two queens threaten each other. 
# The time complexity of O(N!) arises from the fact that for each row, we have to choose a column to place a queen, and we have to ensure that no two queens are in the same column or diagonal.
# In the first row, we have N options (N columns) to place the first queen. Once we place the first queen, we cannot place another queen in the same column or diagonals in the subsequent rows. 
# This restriction reduces the number of available columns for placing queens in the next rows.
# In the second row, we have (N-1) options, 
# in the third row we have (N-2) options, and so on, until we reach the last row where we have only 1 option left. 
# Therefore, the total number of ways to arrange the queens is N * (N-1) * (N-2) * ... * 1 = N!. 

# Space complexity: O(N^2) for the board, Extra auxiliary space: O(1) and recursion stack space: O(N)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        temp = []

        def isValidBoard(row, col):
            # upwards
            for i in range(row-1, -1, -1): # check all rows above the current row
                if board[i][col]=='Q':
                    return False
            
            # right upwards diagonal
            i = row-1
            j = col+1
            while i>=0 and j<n: # check all columns to the right of the current column
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1

            # left upwards diagonal
            i = row-1
            j = col-1
            while i>=0 and j>=0: # check all columns to the left of the current column
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            
            # If we pass the hurdles, return true
            return True
            

        def backtrack(row):
            if row>=n:
                key = board.copy()
                for i in range(n):
                    key[i] = "".join(key[i]) # convert list to string

                res.append(key)
                return

            for col in range(n):
                if isValidBoard(row, col):
                    board[row][col] = 'Q' # place the queen
                    backtrack(row+1) #@ move to the next row
                    board[row][col] = '.' # backtrack

        backtrack(0) # start from the first row

        return res

# Optimized approach using sets to track columns and diagonals
# Same time complexity but still materially better in practice because it reduces the work per node in the search tree and 
# prunes earlier with cheaper checks
# time complexity: O(N!) where N is the size of the board (n x n)

# Space complexity: O(N^2) for the board, Extra auxiliary space: O(N) and recursion stack space: O(N)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        res = []
        temp = [] 
        columns = set()
        diag = set()
        anti_diag = set()           

        def backtrack(row):
            if row>=n:
                key = board.copy()
                for i in range(n):
                    key[i] = "".join(key[i])

                res.append(key)
                return

            for col in range(n): # iterate through all columns
                diag_const = row+col # main_diag_const = row+col which is constant for main diagonal
                anti_diag_const = row-col # anti_diag_const = row-col which is constant for anti diagonal
                if col in columns or diag_const in diag or anti_diag_const in anti_diag: # check if the column or diagonal is already occupied
                    continue
                columns.add(col) # add the column and diagonals to the sets
                diag.add(diag_const) # add main diagonal
                anti_diag.add(anti_diag_const) # add anti diagonal

                board[row][col] = 'Q'
                backtrack(row+1)
                board[row][col] = '.'

                columns.remove(col)
                diag.remove(diag_const)
                anti_diag.remove(anti_diag_const)

        backtrack(0)

        return res
                