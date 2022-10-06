#TITLE: 벽 부수고 이동하기 (https://www.acmicpc.net/problem/2206)
#LEVEL: G4
#TAG: bfs, graphs
#DATE: 20221006
#AUTHOR: squareyun

from collections import deque

n,m=map(int,input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

# [x][y][0]: 벽부수기X, [x][y][1]: 벽부수기O
visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    q = deque()
    visited[0][0][0] = 1
    q.append((0,0,0))

    while q:
        x, y, wallBreak = q.popleft()

        if x == n-1 and y == m-1:
            return visited[x][y][wallBreak]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                if graph[nx][ny] == 1 and wallBreak == 0:
                    visited[nx][ny][1] = visited[x][y][0] + 1 # 벽부수기
                    q.append((nx, ny, 1))
                elif graph[nx][ny] == 0 and visited[nx][ny][wallBreak] == 0:
                    visited[nx][ny][wallBreak] = visited[x][y][wallBreak] + 1
                    q.append((nx, ny, wallBreak))
    return -1
    
print(bfs())