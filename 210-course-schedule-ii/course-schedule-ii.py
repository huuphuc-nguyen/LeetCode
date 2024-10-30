class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        amount_pre = {}

        for i in range(numCourses):
            amount_pre[i] = 0
            graph[i] = []

    
        for course, pre in prerequisites:
            amount_pre[course] += 1
            graph[pre].append(course)

        q = []
        visited = []

        for course in range(numCourses):
            if amount_pre[course] == 0:
                q.append(course)
        
        while q:
            course = q.pop(0)
            visited.append(course)

            for next_course in graph[course]:
                amount_pre[next_course] -= 1
                if amount_pre[next_course] == 0:
                    q.append(next_course)
        
        if len(visited) == numCourses:
            return visited
        else:
            return []

