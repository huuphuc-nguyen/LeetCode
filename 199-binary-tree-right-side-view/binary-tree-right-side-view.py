# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        map = collections.defaultdict(list)

        if not root: return []

        def bfs(node, level):
            if not node: return

            map[level].append(node.val)
            bfs(node.right, level+1)
            bfs(node.left, level+1)

            return
        
        bfs(root,0)

        rs = []

        for arr in map.values():
            rs.append(arr[0])
        
        return rs

