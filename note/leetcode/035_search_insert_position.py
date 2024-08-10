'''
35. Search Insert Position

Easy

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4

'''

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.__searchInsert(nums, 0, len(nums) - 1, target)

    def __searchInsert(self, nums, left, right, target):
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m

            if nums[m] > target:
                r = m
            else:
                l = m + 1

        return l + 1 if nums[l] < target else l
