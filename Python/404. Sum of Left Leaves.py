# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if (not root):
                return 0

            leftRoot = root.left
            rightRoot = root.right

            if (leftRoot and not leftRoot.left and not leftRoot.right):
                return leftRoot.val + dfs(rightRoot)

            return dfs(leftRoot) + dfs(rightRoot)

        return dfs(root)
