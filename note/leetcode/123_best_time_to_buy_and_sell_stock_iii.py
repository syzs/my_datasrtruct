'''
123. Best Time to Buy and Sell Stock III
Hard

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete at most two transactions.

Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

'''


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices: 
            return 0
        n, k = len(prices), 2

        # dp[i][j][0]: 第i天进行了j次交易且不持有股票的最大利润
        # dp[i][j][1]: 第i天进行了j次交易且持有股票的最大利润
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]

        # 初始化状态
        for j in range(k + 1):
            dp[0][j][0] = 0  # 第0天不持有股票，利润为0
            dp[0][j][1] = -prices[0]  # 第0天持有股票，利润为 -prices[0]

        for i in range(1, n):
            for j in range(1, k + 1):  # j 从1开始，0次交易没有意义
                # 第i天不持有股票的最大利润：昨天就不持有或者今天卖出
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                # 第i天持有股票的最大利润：昨天就持有或者今天买入
                dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])

        # 返回最大利润：最后一天不持有股票时的最大利润
        return max(dp[n-1][j][0] for j in range(k + 1))
