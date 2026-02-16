# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.arr = []

        def dfs(root):
            if (not root):
                return

            self.arr.append(root.val)

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        self.arr.sort()

        if (len(self.arr) < 2):
            return 0

        minimumDistance = float("inf")

        for i in range(len(self.arr) - 1):
            minimumDistance = min(
                self.arr[i + 1] - self.arr[i], minimumDistance)

        return minimumDistance
