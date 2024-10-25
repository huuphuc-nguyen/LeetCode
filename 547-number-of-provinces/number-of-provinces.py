class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        count = 0
        visited = []

        def dfs(city):
            for connected_city in range(len(isConnected)):
                if connected_city not in visited and isConnected[city][connected_city] == 1:
                    visited.append(connected_city)
                    dfs(connected_city)

        for city in range(len(isConnected)):
            if city not in visited:
                count += 1
                visited.append(city)
                dfs(city)

        return count

