from collections import deque

class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        count = 0

        while q:
            course = q.popleft()
            count += 1

            for next in graph[course]:
                indegree[next] -= 1

                if indegree[next] == 0:
                    q.append(next)

        return count == numCourses