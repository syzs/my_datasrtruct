'''
51. N-Queens Hard

The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
'''

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        return self.solveNQueens02(n)

    def solveNQueens02(self, n: int) -> List[List[str]]:
        if n < 1: return []

        self.result = []
        self._solve02(0, n, [], [], [])
        return [['.'*i +'Q'+'.'*(n-i-1) for i in cols] for cols in self.result]
    
    # 同列不能有重复数据
    # 主对角线:row-col = c（c为常量）
    # 反对角线：row+col = c
    def _solve02(self, row:int, n:int, cols:List[int], backDiagonal:List[int], leadDiagonal:List[int]):
        if row == n:
            self.result.append(cols)
            return 
        
        for c in range(n):
            if c in cols or row-c in leadDiagonal or row+c in backDiagonal:
                continue
            self._solve02(row+1, n, cols+[c], backDiagonal+[row+c], leadDiagonal+[row-c])

            # !!! 不要在cols...上直接加数据，不然在回溯的过程中，之前的结果会带入到新的计算过程中 !!!
            # cols.append(c)
            # backDiagonal.append(row+c)
            # leadDiagonal.append(row-c)
            # self._solve02(row+1, n, cols, backDiagonal,leadDiagonal)

    def solveNQueens01(self, n: int) -> List[List[str]]:
        if n < 1: return []

        self.nQueuesPrint = []
        for i in range(n):
            self.nQueuesPrint.append("."*(i) + "Q" + "."*(n-i-1))

        self.res = []
        self.order = [-1]*n

        self._solve01(0, n)
        return self.res
    
    def _solve01(self, row, n):
        if row == n:
            self.res.append([self.nQueuesPrint[o] for o in self.order])
            return 
        
        # 判断第 row 行的棋子放在第几列
        for c in range(n):
            if not self.isOK(row, c, n, self.order):
                continue
            self.order[row] = c
            # 判断第 row+1 行的棋子放在第几列
            self._solve01(row+1, n)

    def isOK(self, row:int, column:int,n:int, order: List[int]) -> bool:
        leftup, rightup = column-1, column+1
        for r in range(row-1,-1, -1):
            # 同列、左对角线、右对角线 不能存在Q
            if order[r] in (column, leftup, rightup):return False 
            leftup, rightup = leftup-1, rightup+1

            # 同列
            # if order[r] == column: return False

            # # 左对角线
            # if leftup >=0:
            #     if order[r] == leftup: return False

            # # 有对角线
            # if rightup < n:
            #     if order[r] == rightup: return False
            
            # leftup, rightup = leftup-1, rightup+1
        return True
    
s = Solution()
s.solveNQueens(4)