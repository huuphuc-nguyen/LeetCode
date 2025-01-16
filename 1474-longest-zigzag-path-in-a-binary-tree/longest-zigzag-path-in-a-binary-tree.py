# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if not root:
            return -1
        
        self.max = 0

        def dfs(node, direction, length):
            if not node: return
            
            length += 1
            self.max = max(self.max, length)   

            if direction == "left":
                dfs(node.left, "right", length)
                dfs(node.right, "left", 0)
            else:
                dfs(node.right, "left", length)
                dfs(node.left, "right", 0)
            

        dfs(root,"left",-1)
        dfs(root,"right", -1)
    
        return self.max 