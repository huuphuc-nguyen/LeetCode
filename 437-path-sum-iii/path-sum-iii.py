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
        count = [0]

        # DFS to find paths starting from a specific node
        def dfs(node, current_sum):
            if not node:
                return
            
            # Update the current path sum
            current_sum += node.val
            
            # Check if the current path sum equals the target
            if current_sum == targetSum:
                count[0] += 1
            
            # Recur for left and right children
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
        
        # Traverse every node to use as a starting point
        def traverse(node):
            if not node:
                return
            
            # Start a new DFS from the current node
            dfs(node, 0)
            
            # Recur for left and right children
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return count[0]