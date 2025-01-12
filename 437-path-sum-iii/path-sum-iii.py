# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # count = [0]

        # def dfs(node,current_sum):
        #     if not node:
        #         return
            
        #     current_sum += (node.val)

        #     if current_sum == targetSum:
        #         count[0] += 1
            
        #     dfs(node.left,current_sum)
        #     dfs(node.right, current_sum)
        
        # def traverse(node):
        #     if not node: return

        #     dfs(node,0)
        #     traverse(node.left)
        #     traverse(node.right)


        # traverse(root)

        # return count[0]
        # Dictionary to store prefix sums
        prefix = {0: 1}
        count = 0

        def dfs(node, current_sum):
            nonlocal count
            if not node:
                return
            
            # Update the current path sum
            current_sum += node.val

            # Check if there exists a prefix sum such that current_sum - prefix_sum = targetSum
            count += prefix.get(current_sum - targetSum, 0)

            # Add current_sum to the prefix map
            prefix[current_sum] = prefix.get(current_sum, 0) + 1

            # Recurse for children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)

            # Backtrack: Remove the current sum from the prefix map
            prefix[current_sum] -= 1

        dfs(root, 0)
        return count