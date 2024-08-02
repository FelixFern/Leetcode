# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        nodeVal = []
        
        def bfs(node, depth):
            if(node == None):
                return

            nodeVal.append((node.val, depth))

            bfs(node.left, depth + 1)
            bfs(node.right, depth + 1)

        bfs(root, 0)

        maxDepth = max(i[1] for i in nodeVal)

        return sum(i[0] for i in nodeVal if i[1] == maxDepth)
