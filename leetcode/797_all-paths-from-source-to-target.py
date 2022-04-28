class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(visited, u):
            if u == len(graph) - 1:
                ret.append(visited[:])
                return

            for v in graph[u]:
                visited.append(v)
                dfs(visited, v)
                visited.pop()
        
        ret = []
        dfs([0], 0)
        return ret
    