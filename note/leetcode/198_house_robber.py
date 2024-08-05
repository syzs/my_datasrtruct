'''
198. House Robber

Medium

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

 

Example 1:

Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.rob_dp2(nums)
    
    def rob_recursion(self, nums)->int:
         self.maxValue = nums[0]
         self._recursion(nums, 1, 0, 0)
         self._recursion(nums, 1, nums[0], 1)
         return self.maxValue

    
    # preState: 0抢了；1没抢
    def _recursion(self, nums, i, value, preState):
        if i>=len(nums):
            if self.maxValue < value: self.maxValue=value
            return 
        
        # i-1抢了，i不能抢
        # if preState:
        #     self._recursion(nums,i+1, value, 0)
        # else:
        #     self._recursion(nums, i+1, value+nums[i], 1)
        #     self._recursion(nums, i+1, value, 0)
    
        # 无论前一天有没有抢，今天都可以不抢
        self._recursion(nums, i+1, value, 0)

        if not preState:
            self._recursion(nums, i+1, value+nums[i], 1)

    def rob_dp(self, nums) -> int:
        if not nums: return 0

        n = len(nums)
        # dp[i][j]: i=第i天，j=[0-1],0:不抢劫；1:抢劫
        dp = [[0]*2 for _ in range(n)]
        dp[0][1] = nums[0]

        for i in range(1, n):
            dp[i][0] = max(dp[i-1][1], dp[i-1][0])
            dp[i][1] = dp[i-1][0] + nums[i]
        
        return max(dp[n-1][0], dp[n-1][1])
    
    def rob_dp2(self, nums)->int:
        n = len(nums)
        if not nums  : return 0
        if n <= 1: return nums[0]


        dp = [0]*n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2,n):
            dp[i] = max(dp[i-1], nums[i]+ dp[i-2])
        
        return dp[n-1]