# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        def bfs(root, level, _res):
            if(root == None):
                return 
            
            if(level >= len(_res)):
                _res.append([])

            if(level % 2 == 0):
                _res[level].append(root.val)
            else:
                _res[level] = [root.val] + _res[level]

            bfs(root.left, level + 1, _res)
            bfs(root.right, level + 1, _res)

        bfs(root, 0, res)

        return res