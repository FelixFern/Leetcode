# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        if (not root):
            return []

        def dfs(root, res, paths, targetSum, currSum):
            if not root:
                return

            current_path = paths + [root.val]
            current_sum = currSum + root.val

            if not root.left and not root.right:
                if current_sum == targetSum:
                    res.append(current_path)
                return

            dfs(root.left, res, current_path, targetSum, current_sum)
            dfs(root.right, res, current_path, targetSum, current_sum)

        dfs(root, res, [], targetSum, 0)
        return res
