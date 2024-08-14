'''
209. Minimum Size Subarray Sum

Medium

Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

 

Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0

'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        return self.__minSubArrayLen_loop(target, nums)    

    # 感觉可以但没必要用window
    def __minSubArrayLen_sliding_window(self, target: int, nums: List[int]) -> int:
        if not nums or target <= 0: return 0

        n = len(nums)
        window, subSum, subLenMin = [], 0, n+1

        for i , v in enumerate(nums):
            subSum += v
            window.append(i)

            while window and subSum >= target:
                left = window.pop(0)
                subLenMin = min(subLenMin, i-left+1)
                subSum -= nums[left]
        
        return subLenMin if subLenMin < n+1 else 0



    def __minSubArrayLen_loop(self, target: int, nums: List[int]) -> int:
        if not nums or target <= 0 : return 0

        n = len(nums)
        left, subSum, subLenMin = 0,0, n+1

        for right, v in enumerate(nums):
            subSum += v

            while subSum >= target:
                subLenMin = min(subLenMin, right - left +1)
                subSum -= nums[left]
                left += 1
        
        return subLenMin if subLenMin < n+1 else 0
            



