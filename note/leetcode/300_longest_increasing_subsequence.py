'''
300. Longest Increasing Subsequence
Medium

Given an integer array nums, return the length of the longest strictly increasing 
subsequence


Example 1:

Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Example 2:

Input: nums = [0,1,0,3,2,3]
Output: 4
Example 3:

Input: nums = [7,7,7,7,7,7,7]
Output: 1

'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums: return 0
        # dp[i] = max(dp[j:0..i-1]) + 1 and n[i] > n[j]
        # i 的值，取[0,i-1]中比 n[i]小的数里， 最长的序列+1
        dp = [1] * len(nums) 
        for i in range(1, len(nums) ):
            for j in range(0, i):
                if nums[i] <= nums[j]:
                    continue
                dp[i] = max(dp[i], dp[j]+1)     
        return max(dp)


        