'''
103. Binary Tree Zigzag Level Order Traversal

Medium

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []

        res = []

        dummy = TreeNode()
        dummy.left = root

        queue = collections.deque()
        queue.append(dummy)
        alternate = True

        while queue:
            childQueue = collections.deque()
            nodeChildren = []
            while queue:
                node = queue.popleft()
                      
                if node.left:
                    nodeChildren.append(node.left.val)
                    childQueue.append(node.left)
                if node.right: 
                    nodeChildren.append(node.right.val)
                    childQueue.append(node.right)

            if not alternate: nodeChildren = nodeChildren[::-1]
            if nodeChildren: res.append(nodeChildren)
            
            alternate  = not alternate
            queue = childQueue
        
        return res
                


        