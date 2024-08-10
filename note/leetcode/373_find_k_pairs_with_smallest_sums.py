'''
373. Find K Pairs with Smallest Sums

Medium

You are given two integer arrays nums1 and nums2 sorted in non-decreasing order and an integer k.

Define a pair (u, v) which consists of one element from the first array and one element from the second array.

Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

 

Example 1:

Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
Output: [[1,2],[1,4],[1,6]]
Explanation: The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
Example 2:

Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
Output: [[1,1],[1,1]]
Explanation: The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
'''

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if len(nums1)==0 or len(nums2)==0 or k ==0: return []
        res = []
        minHeap = []

        for i in nums1:
            heapq.heappush(minHeap, [i+nums2[0], 0]) # nums1[i]+nums2[0], nums2.index
        
        while k>0 and minHeap:
            minPair = heapq.heappop(minHeap)
            s, n2Pos = minPair[0], minPair[1]
            res.append([s-nums2[n2Pos], nums2[n2Pos]])

            if n2Pos+1< len(nums2):
                heapq.heappush(minHeap, [s-nums2[n2Pos]+nums2[n2Pos+1], n2Pos+1])
            k -= 1
        
        return res