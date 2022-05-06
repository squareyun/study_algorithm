class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
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
        
        result = []
        for _ in range(numCourses):
            if len(q) == 0:
                return []
            
            course = q.popleft()
            result.append(course)
            
            for i in adjlist[course]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)
        
        return result
