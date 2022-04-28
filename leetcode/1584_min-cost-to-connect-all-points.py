class Solution(object):
    def minCostConnectPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        def find(x):
            if root[x] != x:
                root[x] = find(root[x])
            return root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                root[rootY] = rootX
        
        edges = []
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                edges.append([i, j, weight])
        
        edges.sort(key = lambda x: x[2])
        
        root = [i for i in range(len(points))]
        cost = 0
        tree_edge = 0
        for e in edges:
            v1, v2, weight = e
            if tree_edge == (len(points) - 1):
                break
            if find(v1) != find(v2):
                union(v1, v2)
                cost += weight
                tree_edge += 1
                
        return cost
        