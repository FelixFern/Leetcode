# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def bfs(root, level, res):
            if(len(res) <= level):
                res.append([])

            if(root == None):
                res[level].append(None)
                return

            res[level].append(root.val)

            bfs(root.left, level + 1, res)
            bfs(root.right, level + 1, res)

        
        res = []
        symmetric = True
        bfs(root, 0, res)
        
        for i in res: 
            if(i != i[::-1]):
                symmetric = False
                break

        return symmetric