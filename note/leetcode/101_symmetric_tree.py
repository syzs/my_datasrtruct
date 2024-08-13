'''
101. Symmetric Tree

easy

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return True

        return self.isSame(root.left, root.right)

    
    def isSame(self, left, right) -> bool:
        if not left and not right:return True
        if not left or not right: return False
        if left.val != right.val: return False

        return self.isSame(left.right, right.left) and self.isSame(left.left, right.right)
        