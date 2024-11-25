# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # inorder left -> node -> right

        if not root:
            return []

        result = []

        def dfs(node):
            if not node:
                return
            
            if not node.left and not node.right:
                result.append(node.val)
                return
            
            dfs(node.left)
            result.append(node.val)
            dfs(node.right)
        
        dfs(root)        
        return result