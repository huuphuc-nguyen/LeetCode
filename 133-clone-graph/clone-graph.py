"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """

        if not node:
            return

        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            
            clone = Node(node.val)
            visited[node]= clone

            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))

            return clone
        

        return dfs(node)