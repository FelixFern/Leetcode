# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        nums = []

        def dfs(root, paths):
            if (not root):
                return

            currPath = paths + str(root.val)
            if (not root.left and not root.right):
                nums.append(int(currPath))
                return
            dfs(root.left, currPath)
            dfs(root.right, currPath)

        dfs(root, "")

        return sum(nums)
