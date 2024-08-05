
'''
63. Unique Paths II
Medium

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right
'''

from typing import List

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.uniquePathsWithObstacles_dp(obstacleGrid)

    def uniquePathsWithObstacles_dp(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]: return 0

        m, n  = len(obstacleGrid), len(obstacleGrid[0])
        
        dp = [ [0]*n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1: break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1: break
            dp[0][j] = 1
        
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1] if not obstacleGrid[i][j] else 0
        
        return dp[m-1][n-1]

    # timeout
    def uniquePathsWithObstacles_recursion(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        m, n = len(obstacleGrid)-1, len(obstacleGrid[0])-1
        if obstacleGrid[0][0]  or obstacleGrid[m][n] :
            return 0

        self.res = 0
        self.dfs(obstacleGrid, 0,0, m,n)
        return self.res

    def dfs(self, obstacleGrid, row, col, m,n)-> bool:
        if row == m and col == n:
            self.res += 1
            return

        if obstacleGrid[row][col] == 1:
                return

        if col < n: 
            self.dfs(obstacleGrid, row, col+1, m,n)    
           
        
        if row < m:
            self.dfs(obstacleGrid, row+1, col, m,n)    
            
    

    
        

        