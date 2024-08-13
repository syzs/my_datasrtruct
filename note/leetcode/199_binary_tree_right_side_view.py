'''
199. Binary Tree Right Side View

Medium

Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
Example 2:

Input: root = [1,null,3]
Output: [1,3]
Example 3:

Input: root = [1,2]
Output: [1,2]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
       
        if root is None: return []
          
        result = []

        # 对每一层来说
        #   如果有右节点 -> 只能看到右节点
        #   如果没有右节点 -> 只能看到左节点
        # 只能看到最靠右边的节点 
        queue = collections.deque()
        queue.append(root)

        while queue:
            child_queue = collections.deque()
            prev = -1
            while queue:
                curr = queue.popleft()

                if curr.left: child_queue.append(curr.left)
                if curr.right: child_queue.append(curr.right)
                
                prev = curr
            
            result.append(prev.val)
            queue = child_queue
        
        return result



        

        
        