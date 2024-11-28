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
        string = []
        # key: number, val: node pref => use big, small value to get 2 nodes and change it value
        nodes = {}

        def inorder(node):
            if not node:
                return
            
            inorder(node.left)
            string.append(node.val)
            nodes[node.val] = node
            inorder(node.right)
        
        inorder(root)
        
        # question to ask: could the value of node be negative? if yes => use None if no use -1
        bigvalue = None
        smallvalue = None

        for i in range(len(string) - 1):
            if string[i] > string[i+1]:
                if not bigvalue:
                    bigvalue = string[i] # only get the 1st element that satisfy above confiditon from the left
                smallvalue = string[i+1]
        
        if bigvalue != None and smallvalue != None:
            nodes[bigvalue].val = smallvalue
            nodes[smallvalue].val = bigvalue

        print(nodes)
        