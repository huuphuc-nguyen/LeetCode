class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        
        hashmap = {}

        for row in wall:
            edge_position = 0
            for brick in row[:-1]:
                edge_position += brick
                if edge_position in hashmap:
                    hashmap[edge_position] += 1
                else:
                    hashmap[edge_position] = 1

        max_edges = max(hashmap.values()) if hashmap else 0

        return len(wall) -  max_edges