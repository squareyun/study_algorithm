import heapq

class Solution(object):
    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        
        graph = [[] for i in range(n+1)]
        for t in times:
            graph[t[0]].append((t[1], t[2]))
        
        INF = 987654321
        distance = [INF] * (n+1)
        
        q = []
        heapq.heappush(q, (0, k))
        distance[k] = 0
        while q:
            dist, now = heapq.heappop(q)
            
            if dist > distance[now]:
                continue
            
            for i in graph[now]:
                cost = i[1] + dist
                
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))
        
        if INF in distance[1:]:
            return -1
        return max(distance[1:])
        