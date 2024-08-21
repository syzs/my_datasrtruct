'''
4. Median of Two Sorted Arrays

Hard

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        return self.findMedianSortedArrays_merge(nums1, nums2)

    def findMedianSortedArrays_merge(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total = m + n
        midIndex = [total//2]
        if total % 2 == 0: midIndex.append(total//2-1)

        i, j = 0, 0
        mergeIndex = -1
        sumValue, tmp = 0, 0
        while (i < m or j < n) and mergeIndex <= total//2:
            if j >= n or (i < m and  nums1[i] < nums2[j]):
                tmp = nums1[i]
                i += 1
            elif i >= m or ( j < n and nums1[i] >= nums2[j]):
                tmp = nums2[j]
                j += 1
            
            mergeIndex += 1
            if mergeIndex in midIndex: sumValue += tmp
        
        return sumValue/len(midIndex)


        