'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        return self.twoSum_binarySearch(numbers, target)
        
    def twoSum_binarySearch(self, numbers:List[int], target:int) -> List[int]:
        for i, n in enumerate(numbers):
            targetIndex = self.bs(numbers, i+1, len(numbers)-1, target-n)
            if  targetIndex > i:  return [i+1, targetIndex+1]
        return []

    def bs(self, numbers:List[int], left:int, right:int, target:int) -> int:
        mid = (left+right)//2
        while left<=right:   
            mid = (left+right)//2    
            if numbers[mid] == target:
                return mid
            if numbers[mid] > target:
                right = mid-1
                continue
            if numbers[mid] < target:
                left = mid+1         
        return -1

    def towSum_map(self, numbers: List[int], target: int) -> List[int]:
        numbersDict = {}
        for i,n in enumerate(numbers):
            numbersDict[n] = i
        
        for i,n in enumerate(numbers):
            targetIndex = numbersDict.get(target-n, -1)
            if targetIndex > i:
                return [i+1, targetIndex+1]
