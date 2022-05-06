from collections import deque

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjlist = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        
        for a, b in prerequisites:
            adjlist[b].append(a)
            indegree[a] += 1
        
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        
        for _ in range(numCourses):
            if len(q) == 0:
                return False
            
            course = q.popleft()
            
            for i in adjlist[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return True
