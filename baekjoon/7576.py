#TITLE: 토마토 (https://www.acmicpc.net/problem/7576)
#LEVEL: G5
#TAG: graphs, graph_traversal, bfs
#DATE: 20220923
#AUTHOR: squareyun

from collections import deque

m,n=map(int,input().split())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
graph=[]
visited=[]
q = deque()
for i in range(n):
    t = list(map(int,input().split()))
    graph.append(t)
    visited.append([False] * m)
    for j in range(m):
        if graph[i][j] == 1:
            q.append((i, j))
            visited[i][j] = True

def bfs():
    ret = -1
    while q:
        x, y = q.popleft()
        ret = max(ret, graph[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] != -1:
                    visited[nx][ny] = True
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx, ny))
    for i in range(n):
        if 0 in graph[i]:
            return -1
    return ret-1

print(bfs())