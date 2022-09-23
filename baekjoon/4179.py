#TITLE: 불! (https://www.acmicpc.net/problem/4179)
#LEVEL: G4
#TAG: graphs, graph_traversal, bfs
#DATE: 20220923
#AUTHOR: squareyun

from collections import deque
r, c = map(int, input().split())
dx = [0, 0, 1, -1] #동서남북
dy = [1, -1, 0, 0]
graph = []
fire = deque()
jihoon = deque()
dist_f = []
dist_j = []
for i in range(r):
    t = list(input())
    dist_f.append([-1] * c)
    dist_j.append([-1] * c)
    for j in range(c):
        if t[j] == 'F':
            fire.append((i, j))
            dist_f[i][j] = 1
        if t[j] == 'J':
            jihoon.append((i, j))
            dist_j[i][j] = 1
    graph.append(t)

def bfs():
    while fire:
        x, y = fire.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c:
                if dist_f[nx][ny] >= 0 or graph[nx][ny] == '#': continue
                dist_f[nx][ny] = dist_f[x][y] + 1
                fire.append((nx, ny))
    while jihoon:
        x, y = jihoon.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if not(0<=nx<r) or not(0<=ny<c):
                return dist_j[x][y]
            else:
                if dist_j[nx][ny] >= 0 or graph[nx][ny] == '#': continue
                if dist_j[x][y] + 1 < dist_f[nx][ny] or dist_f[nx][ny] == -1:
                    dist_j[nx][ny] = dist_j[x][y] + 1
                    jihoon.append((nx,ny))
    return 'IMPOSSIBLE'
print(bfs())