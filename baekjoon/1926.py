#TITLE: 그림 (https://www.acmicpc.net/problem/1926)
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
    graph.append(list(map(int,input().split())))
    visited.append([False] * m)

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 0
    while q:
        x, y = q.popleft()
        cnt += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return cnt

total = 0
max_num = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1 and not visited[i][j]:
            max_num = max(max_num, bfs(i, j))
            total += 1
print(total)
print(max_num)