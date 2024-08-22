# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        childNode = {}
        leaves = []
        nodes = []
        res = 0
        def bfs(parents, node, depth):
            depth += 1
            if(node == None):
                return
            nodes.append(0)
            for i in parents:
                if(childNode.get(i, []) == []):
                    childNode[i] = [node.val]
                else: 
                    childNode[i].append(node.val)

            newParents = parents[:]
            newParents.append((node.val, depth, len(nodes)))

            if(node.left == None and node.right == None):
                leaves.append(0)
                return
            bfs(newParents, node.left, depth)
            bfs(newParents, node.right, depth)

        bfs([], root, 0)
        for i in childNode:
            res += ((sum(childNode[i]) + i[0]) // (len(childNode[i]) + 1)) == i[0]

        return res + len(leaves)