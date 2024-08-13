'''
530. Minimum Absolute Difference in BST

Easy

Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.

Input: root = [4,2,6,1,3]
Output: 1

Input: root = [1,0,48,null,null,12,49]
Output: 1

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        if not root: return None

        self.min = 10**5
        self.prev = None
        # 中序遍历的结果是 排序 的
        return self.getMin(root)

    
    def getMin(self, root):
        if not root: return self.min

        self.getMin(root.left)

        # if self.prev # 0 也不会命中
        if self.prev is not None:
            self.min = min(self.min, root.val - self.prev)
        self.prev = root.val

        self.getMin(root.right)

        return self.min
