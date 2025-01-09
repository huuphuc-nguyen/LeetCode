# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # function(root) -> arr
        # return arr1 == arr2

        # inorder search => L N R


        if not root1 or not root2:
            return

        arr1 = []
        arr2 = []

        def dfs(node, arr):
            if not node:
                return
            # check for leaf
            if not node.left and not node.right:
                arr.append(node.val)
                return
            
            # Left
            dfs(node.left, arr)

            # Node
            # do nothing

            # Right
            dfs(node.right, arr)
        
        dfs(root1, arr1)
        dfs(root2, arr2)

        return arr1 == arr2


