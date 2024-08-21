'''
34. Find First and Last Position of Element in Sorted Array
Medium
Topics
Companies
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]

'''


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1, -1]
        if not nums: return res

        left, right = 0, len(nums)-1

        # 让left在 第一个 target的 index 上
        while left < right: # left 不可以 = right
            mid = left + (right-left) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                right = mid

        if nums[left] != target:
            return res

        res[0], res[1] = left, left

        right = len(nums)-1
        while left <= right:
            mid = left + (right- left) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1 # left=mid 无法使mid往后移

        res[1] = right
        return res