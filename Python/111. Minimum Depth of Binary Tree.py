# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if(not root):
            return 0
            
        def bfs(root, level):
            if(root == None):
                return float('inf')
            if(not root.left and not root.right):
                return level

            return min(bfs(root.left, level + 1), bfs(root.right, level + 1))
        
        return bfs(root, 1)