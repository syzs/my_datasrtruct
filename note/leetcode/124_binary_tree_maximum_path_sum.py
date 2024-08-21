'''
124. Binary Tree Maximum Path Sum
Solved
Hard
Topics
Companies
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

Example1:

Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        self.ans = float('-inf')

        def post(root):
            if not root: return 0

            lSum, rSum = post(root.left), post(root.right)
            # sMax = max(root.val, root.val + max(lSum, rSum), root.val + lSum + rSum)
            # 只能选择左子树或右子树向下延伸的最大路径和。这个值将在其父节点继续计算时使用。对于父节点来说，它只能选择当前节点的左子树路径或者右子树路径之一，而不能同时选择两者。因此，返回值不能包含同时经过左右子树的路径
            sMax = max(root.val, root.val + max(lSum, rSum))
            self.ans = max(self.ans, sMax, root.val + lSum + rSum)
            return sMax

        post(root)
        return self.ans