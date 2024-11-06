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


            if node.left is None and node.right is None:
                mylist.append(node.val)
                if sum(mylist) == targetSum:
                    result.append(mylist)

            print(mylist)

            dfs(node.left, mylist + [node.val])
            dfs(node.right, mylist + [node.val])
        
        dfs(root, [])

        return result

        
            
        




        