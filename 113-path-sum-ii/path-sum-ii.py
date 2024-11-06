# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: List[List[int]]
        """

        result = []
        def dfs(node, mylist):
            if node is None:
                return

            mylist.append(node.val)

            if node.left is None and node.right is None:
                if sum(mylist) == targetSum:
                    result.append(list(mylist)) 

            dfs(node.left, mylist)
            dfs(node.right, mylist)

            mylist.pop()
        
        dfs(root, [])

        return result

        
            
        




        