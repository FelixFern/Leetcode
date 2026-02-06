from collections import deque as queue
"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if (not root):
            return []

        q = queue()
        q.append(root)
        res = []

        while (len(q) > 0):
            levelSize = len(q)
            level = []
            for i in range(levelSize):
                curr = q.popleft()
                level.append(curr.val)

                if (curr.children):
                    for j in curr.children:
                        q.append(j)

            res.append(level)

        return res
