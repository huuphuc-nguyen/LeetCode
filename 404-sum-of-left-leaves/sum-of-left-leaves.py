# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        # Base case: if the root is None, there are no leaves
        if not root:
            return 0

        # Initialize sum to 0
        sum_left_leaves = 0

        # Check if the left child is a leaf node
        if root.left and not root.left.left and not root.left.right:
            # Add the value of the left leaf to sum
            sum_left_leaves += root.left.val

        # Recursively call the function on the left and right children
        sum_left_leaves += self.sumOfLeftLeaves(root.left)
        sum_left_leaves += self.sumOfLeftLeaves(root.right)

        return sum_left_leaves