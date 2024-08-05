'''
322. Coin Change

Medium

Companies
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.

 

Example 1:

Input: coins = [1,2,5], amount = 11
Output: 3
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
'''

class Solution:
    '''
    1. 和爬楼梯的类似，一次可以爬的阶梯数为 coins 次，f(n) = f(amount-coins)，
        从大的coins开始递归，减少递归层数
    2.贪心，并不总能得到最优解
    3.dp，0-1 背包问题的变形
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins: return -1

        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for i in range(1, amount+1):
            for j in range(0, len(coins)):
                # coins[j] 的面值需 < 当前要合成的面值
                if coins[j] > i:
                    continue
                dp[i] = min(dp[i], dp[i-coins[j]] + 1)
        
        return dp[amount] if dp[amount] <= amount else -1