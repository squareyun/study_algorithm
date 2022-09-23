#TITLE: 불 (https://www.acmicpc.net/problem/5427)
#LEVEL: G4
#TAG: graphs, graph_traversal, bfs
#DATE: 20220923
#AUTHOR: squareyun

from collections import deque

num_test = int(input())
dx = [0, 0, 1, -1] #동서남북
dy = [1, -1, 0, 0]

def bfs():
    cycle = 0
    while person:
        cycle += 1
        while fire and fire[0][2] < cycle:
            x, y, c = fire.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.' or board[nx][ny] == '@':
                        board[nx][ny] = '*'
                        fire.append((nx, ny, c + 1))
        
        while person and person[0][2] < cycle:
            x, y, c = person.popleft()
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < h and 0 <= ny < w:
                    if board[nx][ny] == '.' and not visited[nx][ny]:
                        visited[nx][ny] = True
                        person.append((nx, ny, c + 1))
                else:
                    return cycle
    return 'IMPOSSIBLE'

for _ in range(num_test):
    w, h = map(int, input().split())
    board = []
    visited = [[False] * w for _ in range(h)]
    fire = deque()
    person = deque()
    for i in range(h):
        t = list(input())
        if '*' in t:
            for j in range(w):
                if t[j] == '*': fire.append((i, j, 0)) #(fire.x, fire.y, cycle)
        if '@' in t:
            person.append((i, t.index('@'), 0)) #(person.x, person.y, cycle)
        board.append(t)
    print(bfs())