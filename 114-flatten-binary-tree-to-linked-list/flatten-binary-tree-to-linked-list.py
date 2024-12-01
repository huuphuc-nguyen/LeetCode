# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        dummy = TreeNode(0)
        current = dummy

        def dfs(node):
            nonlocal current
            if not node:
                return

            current.right = TreeNode(node.val)
            current = current.right
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        root.left = None
        root.right = dummy.right.right

        