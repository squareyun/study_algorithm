class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        adjList = collections.defaultdict(list)
        for i, j in edges:
            adjList[i].append(j)
            adjList[j].append(i)
        
        stack = [source]
        visited = set()
        
        while stack:
            cur = stack.pop()
            if cur in visited:
                continue
            if cur == destination:
                return True
            visited.add(cur)
            for i in adjList[cur]:
                stack.append(i)
        
        return False
        