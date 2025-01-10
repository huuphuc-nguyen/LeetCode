# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return

        count = [1]

        def dfs(node, max_val_of_path):
            if not node:
                return

            max_val_of_path = max(max_val_of_path, node.val)

            if node.right and node.right.val >= max_val_of_path:
                count[0] += 1
            if node.left and node.left.val >= max_val_of_path:
                count[0] += 1

            dfs(node.right,max_val_of_path)
            dfs(node.left, max_val_of_path)

        dfs(root, root.val)

        return count[0]
        