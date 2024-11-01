class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        import heapq

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))
        
        distances = defaultdict(int)
        for i in range(1,n+1):
            distances[i] = float('inf')

        q=[(0,k)]
        distances[k] = 0

        while q:
            current_dis, node =heapq.heappop(q)
            if current_dis > distances[node]:
                continue
            
            for next, weight in graph[node]:
                distance = current_dis + weight
                if distance < distances[next]:
                    distances[next] = distance
                    heapq.heappush(q,(distance, next))

        max_distance = max(distances.values())
        return max_distance if max_distance < float('inf') else -1
