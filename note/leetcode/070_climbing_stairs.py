'''
70. Climbing Stairs Easy

You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
'''
class Solution:

    def __init__(self):
        self.cacheMap = {0:1,1:1}

    def climbStairs(self, n: int) -> int:
        return self.climbStairs_fb(n)

    def climbStairs_fb(self, n: int) -> int:
        if n <= 1:
            return n
        x, y = 1,1
        for i in range(1, n):
            x, y = y, x+y
        return y

    def climbStairs_bk(self, n: int) -> int:
        if n in self.cacheMap:
            return self.cacheMap[n]
        
        self.cacheMap[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.cacheMap[n]
        