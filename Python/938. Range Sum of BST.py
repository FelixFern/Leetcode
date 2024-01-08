
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

root = TreeNode()
low = 0
high = 10

global sums
sums = 0

if (low <= root.val <= high):
    sums += root.val


def bfs(root, low, high):
    global sums
    if (root.left != None):
        if (low <= root.left.val <= high):
            sums += root.left.val
        bfs(root.left, low, high)
    if (root.right != None):
        if (low <= root.right.val <= high):
            sums += root.right.val
        bfs(root.right, low, high)


bfs(root, low, high)
return sums
