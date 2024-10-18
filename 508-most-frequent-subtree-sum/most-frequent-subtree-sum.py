# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        hashmap = collections.defaultdict(int)

        def sum(node):
            if not node:
                return 0
            
            if not node.left and not node.right:
                hashmap[node.val] += 1
                return node.val
            
            # Calculate sum on left and right first, and then the node it self
            left_sum = sum(node.left) # this do 2 things, 1st put the sum it selft to list, 2nd get the sum of subtree
            right_sum = sum(node.right)

            # Check if current node doesn't have left or child
            current_sum = node.val + left_sum +  right_sum 

            hashmap[current_sum] += 1

            return current_sum
        
        sum(root)

        maxFreq = max(hashmap.values())
        
        result = []

        for key in list(hashmap.keys()):
            if hashmap[key] == maxFreq:
                result.append(key)

        return result



        