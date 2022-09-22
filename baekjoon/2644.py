#TITLE: 촌수계산 (https://www.acmicpc.net/problem/2644)
#LEVEL: Silver 2
#TAG: graphs, graph_traversal, bfs
#DATE: 20220922
#AUTHOR: squareyun

from collections import deque

n = int(input())
graph = [[] * (n+1) for _ in range(n+1)]
visited = [False] * (n+1)
s,e=map(int,input().split())
m=int(input())
for _ in range(m):
    x, y = map(int,input().split())
    graph[x].append(y)
    graph[y].append(x)

def bfs(s, e):
    q = deque()
    q. append((s,0))
    while q:
        node, cnt = q.popleft()

        if node == e:
            return cnt

        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                q.append((i, cnt+1))
    return -1

print(bfs(s, e))