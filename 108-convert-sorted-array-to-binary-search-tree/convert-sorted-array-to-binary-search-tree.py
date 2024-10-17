# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: Optional[TreeNode]
        """
        if not nums:
            return None
        mid_i = len(nums) // 2
        root = TreeNode(nums[mid_i])

        root.left = self.sortedArrayToBST(nums[:mid_i])
        root.right = self.sortedArrayToBST(nums[mid_i+1:])

        return root