'''
37. Sudoku Solver Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.


'''

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solveSudoku01(board)
        # self.solveSudoku02(board)
        return

    def solveSudoku02(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        self.solve02(board, 0, 0, len(board))
        return 
        
    def solve02(self, board, row, col, n)-> bool:
        
        if row == n:
            return True
        if col == n:
            return self.solve02(board, row+1, 0, n)
        
        if board[row][col] == ".":
            for i in range(1,n+1):
                if self.isValid(board, row, col, str(i)):
                    board[row][col] = str(i)

                    if self.solve02(board, row, col+1, n):
                        return True
                    else:
                        board[row][col] = '.'
            return False
        else:
            return self.solve02(board, row, col+1, n)


    def solveSudoku01(self, board: List[List[str]]) -> None:
        if not board:
            return
        
        self.solve01(board)
        return 
    
    def solve01(self, board) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == '.':
                    for c in range(1,10):
                        cc = str(c)
                        if self.isValid(board, i, j, cc):
                            board[i][j] = cc
                            if self.solve01(board):
                                return True
                            else:
                                board[i][j] = '.' # board[i][j] = cc 赋值操作后，solve 未成功，需要撤回赋值操作
                    # . 的情况下，遍历放置了 1-9，都不成功，则返回失败
                    return False
        
        return True
    
    def isValid(self, board, row, col, cc):
        for i in range(len(board)):
            # check row
            if board[row][i] == cc: return False
            # check column
            if board[i][col] == cc: return False
            # check 3*3
            if board[3*(row//3) + i//3][3*(col//3) + i%3] == cc: return False
        return True
