'''
230. Kth Smallest Element in a BST

Medium

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or k <= 0: return None
        self.count = 0
        return self.inOrder(root, k)


    def inOrder(self, root, k):
        if not root: return -1

        v = self.inOrder(root.left, k)
        if v != -1:
            return v

        self.count += 1
        if self.count == k :
            return root.val

        return self.inOrder(root.right, k)