#TITLE: 뱀 (https://www.acmicpc.net/problem/3190)
#LEVEL: G4
#TAG: implementation, simulation, queue
#DATE: 20221006
#AUTHOR: squareyun

from collections import deque

n=int(input())
k=int(input())
graph=[[0] * n for _ in range(n)]
for _ in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1] = 2 #사과 위치
l=int(input())
logs=[]
for _ in range(l):
    a,b=input().split()
    logs.append([int(a),b])

dx = [0, -1, 0, 1] #동북서남
dy = [1, 0, -1, 0]

def solution():
    cnt = 0
    logIdx = 0
    x, y = 0, 0
    dir = 0
    graph[0][0] = 1
    snake=deque([(0,0)])
    while True:
        cnt += 1
        nx = x + dx[dir]
        ny = y + dy[dir]
        
        if logIdx < len(logs) and cnt == logs[logIdx][0]:
            if logs[logIdx][1] == 'L':
                dir = (dir + 1) % 4
            else:
                dir = (dir - 1) % 4
            logIdx += 1

        if 0 > nx or nx >= n or 0 > ny or ny >= n: #벽에 부딪힐 때
            return cnt
        elif graph[nx][ny] == 1: #자기자신의 몸과 부딪힐 때
            return cnt
        elif graph[nx][ny] == 2: #사과 만날 때
            graph[nx][ny] = 1
            snake.append((nx,ny))
        else:
            graph[nx][ny] = 1
            snake.append((nx,ny))
            graph[snake[0][0]][snake[0][1]] = 0
            snake.popleft()

        x, y = nx, ny

print(solution())