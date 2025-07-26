# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def count(node, depth):
            if not node:
                return depth - 1
            if not node.left and node.right is None:
                return depth
            return max( count(node.left, depth + 1)
            ,count(node.right, depth + 1))

        return count(root,1)
        