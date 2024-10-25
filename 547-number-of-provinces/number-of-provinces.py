class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        visited = []
        count = 0

        def dfs(city):
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and neighbor not in visited:
                    visited.append(neighbor)
                    dfs(neighbor)

        for city in range(len(isConnected)):
            if city not in visited:
                count += 1
                visited.append(city)

                dfs(city)
        
        return count

        


