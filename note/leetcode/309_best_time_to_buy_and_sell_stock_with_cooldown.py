'''
309. Best Time to Buy and Sell Stock with Cooldown

Medium

You are given an array prices where prices[i] is the price of a given stock on the ith day.

Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [1,2,3,0,2]
Output: 3
Explanation: transactions = [buy, sell, cooldown, buy, sell]
'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        n = len(prices)
        '''
        hold[i]: 第 i 天持有股票的最大利润。
        sold[i]: 第 i 天卖出股票的最大利润。
        cooldown[i]: 第 i 天处于冷冻期或不操作的最大利润。
        '''

        hold = [0] * n
        sold = [0] * n
        cooldown = [0] * n

        # 初始化
        hold[0] = -prices[0]  # 第一天买入股票
        sold[0] = 0  # 第一天卖不出去
        cooldown[0] = 0  # 第一天冷冻期为0

        for i in range(1, n):
            # 当天持有股票的最大利润是前一天继续持有股票或在冷冻期买入股票。
            hold[i] = max(hold[i-1], cooldown[i-1] - prices[i])
            # 当天卖出股票的最大利润是前一天持有股票后卖出。
            sold[i] = hold[i-1] + prices[i]
            # 当天处于冷冻期的最大利润是前一天已经处于冷冻期或前一天卖出股票。
            cooldown[i] = max(cooldown[i-1], sold[i-1])
        
        # 最后一天不持有股票的最大利润，最后一天卖出了或处于冷静期
        return max(sold[-1], cooldown[-1])