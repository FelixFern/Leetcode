# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        resNodes = []
        def traverse(gp, prevNodeVal, tree):
            if(tree == None):
                return
            
            if(gp):
                if(gp % 2 == 0 ):
                    resNodes.append(tree.val)
                
            traverse(prevNodeVal, tree.val, tree.right)
            traverse(prevNodeVal, tree.val, tree.left)
        
        traverse(None, None, root)
        return sum(resNodes)



            