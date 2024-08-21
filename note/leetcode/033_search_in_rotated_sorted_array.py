'''
33. Search in Rotated Sorted Array

Medium

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

'''

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.search_binary(nums, target)

    def search_binary(self, nums: List[int], target: int) -> int:
        if not nums: return -1

        n = len(nums)
        left, right = 0, n-1

        # 找到最小的值，即 rotate 的 index
        while left < right:
            mid = left + (right- left) // 2
            if nums[mid] > nums[right]: 
                left = mid+1
            else:
                right = mid

        # left == right 是最小索引
        rot = left
        left, right = 0, n-1

        while left <= right:
            mid = left + (right-left)//2
            # ???
            realmid = (rot+mid)%n

            if nums[realmid]==target: return realmid
            if nums[realmid] < target: left = mid+1
            else:right=mid-1
        return -1