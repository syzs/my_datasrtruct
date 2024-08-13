'''
637. Average of Levels in Binary Tree

Easy

Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root: return []

        queue =  collections.deque()
        queue.append(root)

        res = []

        while queue:
            count  = 0
            sumValue = 0
            childQueue = collections.deque()
            while queue:
                node = queue.popleft()
                sumValue += node.val
                count += 1
                if node.left: childQueue.append(node.left)
                if node.right: childQueue.append(node.right)

            queue = childQueue
            res.append(sumValue/count)
        
        return res
        


        