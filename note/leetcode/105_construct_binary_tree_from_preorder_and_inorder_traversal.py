'''

105. Construct Binary Tree from Preorder and Inorder Traversal

Medium

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.


Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: preorder = [-1], inorder = [-1]
Output: [-1]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder or len(preorder) != len(inorder): return None
        return self.__buildTree(preorder, 0, len(preorder)-1, inorder, 0, len(inorder)-1)

    def __buildTree(self, preorder: List[int], preStart, preEnd,  inorder: List[int], inStart, inEnd):
        if preStart > preEnd or inStart > inEnd: return None

        root = TreeNode(val=preorder[preStart])

        # 确认root节点在中序遍历中的索引
        rootIndex = -1
        for i in range(inStart, inEnd+1):
            if inorder[i] == root.val:
                rootIndex = i
                break
        
        # 确定左右子树的节点个数
        leftNodeCount = rootIndex - inStart
        rightNodeCount = inEnd - rootIndex

        root.left = self.__buildTree(preorder, preStart+1, preStart + leftNodeCount, inorder, inStart, rootIndex-1)
        root.right = self.__buildTree(preorder, preStart+leftNodeCount+1, preEnd, inorder, rootIndex+1, inEnd)

        return root

        