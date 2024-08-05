'''
64. Minimum Path Sum

Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.

'''

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        if not grid: return 0

        path = [ [0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

        sum = 0
        # 初始化第一行和第一列
        for i in range(len(grid[0])):
            sum += grid[0][i]
            path[0][i] = sum
        sum = 0
        for j in range(len(grid)):
            sum +=grid[j][0]
            path[j][0] = sum

        for i in range(1, len(grid)):
            for j in range(1, len(grid[0])):
                path[i][j] = grid[i][j] + min(path[i-1][j], path[i][j-1])
        
        return path[-1][-1]


        

        # for i in range(len(grid)-2, -1, -1):
        #     for j in range(len(grid[0])):
        #         path[j] = grid[i][j] + min(path[j], path[j+1])
        
        # return path[0]

        