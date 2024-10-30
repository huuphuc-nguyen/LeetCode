class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        graph = {}
        degree = {}

        for i in range(numCourses):
            graph[i] = []
            degree[i] = 0

        for course, pre in prerequisites:
            graph[pre].append(course)
            degree[course] += 1

        q =[]
        visited =[]

        for i in range(numCourses):
            if degree[i] == 0:
                q.append(i)
        
        while q:
            course = q.pop(0)
            visited.append(course)

            for next_course in graph[course]:
                degree[next_course] -= 1
                if degree[next_course] == 0:
                    q.append(next_course)
        if len(visited) == numCourses:
            return visited
        else:
            return []



        
