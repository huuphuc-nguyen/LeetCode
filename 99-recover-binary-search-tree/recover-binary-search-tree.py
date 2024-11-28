# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        nodes = []

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            nodes.append(node)
            inorder(node.right)
        
        inorder(root)
        
        # question to ask: could the value of node be negative? if yes => use None if no use -1
        bigvalue = None
        smallvalue = None

        for i in range(len(nodes) - 1):
            if nodes[i].val > nodes[i+1].val:
                if not bigvalue:
                    bigvalue = nodes[i] # only get the 1st element that satisfy above confiditon from the left
                smallvalue = nodes[i+1]
        
        if bigvalue and smallvalue:
            bigvalue.val, smallvalue.val = smallvalue.val, bigvalue.val
   