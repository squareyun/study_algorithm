#TITLE: 미로 탐색 (https://www.acmicpc.net/problem/2178)
#LEVEL: S1
#TAG: graphs, graph_traversal, bfs
#DATE: 20220923
#AUTHOR: squareyun

from collections import deque

n,m=map(int,input().split())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
graph=[]
visited=[]
for _ in range(n):
    graph.append(list(map(int, input())))
    visited.append([False] * m)

def bfs():
    q = deque([(0, 0, 1)])
    while q:
        x, y, cnt = q.popleft()

        if x == n-1 and y == m-1:
            return cnt
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if not visited[nx][ny] and graph[nx][ny] == 1:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
print(bfs())