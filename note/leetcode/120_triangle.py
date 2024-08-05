'''
120. Triangle
Medium

Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current row, you may move to either index i or index i + 1 on the next row.

 

Example 1:

Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
Output: 11
Explanation: The triangle looks like:
   2
  3 4
 6 5 7
4 1 8 3
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).
Example 2:

Input: triangle = [[-10]]
Output: -10
'''

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle: return 0

        # 把最后一行的值直接赋值给 res，作为初始化的数据
        # [4,1,8,3]
        res = triangle[-1]

        # 从下往上递推
        # 从倒数第二行开始往上递推
        for i in range(len(triangle)-2, -1, -1):
            # [6,5,7] 计算到达 6、5、7 的最短距离
            for j in range(0, len(triangle[i])):# 6->5->7
                # 计算到6的最短距离，即计算它可达的两个点的大小，并加上它本身
                # min(res[j], res[j+1] 里的数据是上一层的数据
                res[j] = triangle[i][j] + min(res[j], res[j+1])
        
        return res[0]
        