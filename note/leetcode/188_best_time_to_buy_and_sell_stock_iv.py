'''
188. Best Time to Buy and Sell Stock IV

Hard

You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

'''

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        if not prices: return 0

        n = len(prices)

        # dp[i][k][j]: 第i天的第k次交易是否持有股票
        dp = [ [ [0]*2 for _ in range(k+1)] for _ in range(n)]

        # 初始化第一天交易的数据
        for j in range(k+1):
            dp[0][j][0] = 0
            dp[0][j][1] = -prices[0]

        for i in range(1, n):
            for j in range(1, k+1):
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        
        return max(dp[n-1][j][0] for j in range(k+1))
