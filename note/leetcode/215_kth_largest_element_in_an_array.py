'''
215. Kth Largest Element in an Array

Medium

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 

Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4
'''

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.__findKLagest_heap(nums, k)
    
    def __findKLagest_heap(self, nums:List[int], k:int) -> int:
        klargest = nums[:k]
        heapq.heapify(klargest)
        
        for i in range(k, len(nums)):
            if nums[i] < klargest[0]:
                continue
            heapq.heappop(klargest)
            heapq.heappush(klargest, nums[i])
            
        return klargest[0]
    

    # 40 / 41 testcases passed，数据量太大，递归深度太高
    def __findKthLargest_quicksort(self, nums:List[int], k:int)->int:
        if len(nums) < k : return -1
        return self.__quicksort_recursion(nums, k, 0, len(nums)-1)

    def __quicksort_recursion(self, nums:List[int], k:int, low:int, height:int)->int:
        if low >= height: return nums[low]
        pivot = nums[height]
        # i 记录的是有多少个比 pivot 大
        i = low
        for j in range(low, height):
            if nums[j] > pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        nums[i], nums[height] = nums[height], nums[i]
        if i == k-1:
            return nums[k-1]
        
        
        if i > k-1:
            return self.__quicksort_recursion(nums, k, low, i-1)
        else:
            return self.__quicksort_recursion(nums, k, i+1, height)

     

    def __quicksort_sort(self, nums:List[int], k:int) -> int:
        if len(nums) < k: return -1
        nums.sort(reverse=True)
        return nums[k-1]
