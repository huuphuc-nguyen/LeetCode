# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node):
            if not node:
                return 0
            
            right_high = dfs(node.right)
            left_high = dfs(node.left)
            max_children_high = max(right_high, left_high)
            return max_children_high + 1
        
        return dfs(root)



        