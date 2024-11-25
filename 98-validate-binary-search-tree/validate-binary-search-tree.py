# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node,min,max):
            
            if not node:
                return True
            
            # incorrect order of parent and children:
            if node.left and node.left.val > node.val:
                return False
            if node.right and node.right.val < node.val:
                return False
            
            # root of current subtree must be < than max
            if node.val >= max:
                return False
            
            if node.val <= min:
                return False
            
            return dfs(node.left,min,node.val) and dfs(node.right,node.val,max)

        return dfs(root,float('-inf'), float('inf'))
            