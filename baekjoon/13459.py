# TITLE: 구슬 탈출 (https://www.acmicpc.net/problem/13459)
# LEVEL: Gold 2
# TAG: bfs, implementation, simulation, samsung 
# DATE: 20220807
# AUTHOR: squareyun

from collections import deque

N,M=map(int,input().split())
board=[[[] for _ in range(M)] for _ in range(N)]
q = deque()
visited=[]
rx,ry,bx,by=0,0,0,0
for i in range(N):
    board[i] = list(input())
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j
q.append((rx,ry,bx,by,1))
visited.append((rx,by,bx,by))

dx=[-1,0,1,0] #URDL
dy=[0,1,0,-1]

def move(x,y,dx,dy):
    count = 0
    while board[x+dx][y+dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1
    return x,y,count
        
def bfs():
    while q:
        rx, ry, bx, by, depth = q.popleft()
        
        if depth > 10:
            print(0); return

        for i in range(4):
            nrx,nry,rcnt=move(rx,ry,dx[i],dy[i])
            nbx,nby,bcnt=move(bx,by,dx[i],dy[i])

            if board[nbx][nby] == 'O': #실패 케이스
                continue
            if board[nrx][nry] == 'O': #성공 케이스
                print(1); return

            if nrx==nbx and nry==nby: #같은 위치일 때
                if rcnt>bcnt: #더 멀리있는 구슬이 한 칸 뒤로
                    nrx-=dx[i]; nry-=dy[i]
                else:
                    nbx-=dx[i]; nby-=dy[i]

            if (nrx,nry,nbx,nby) not in visited:
                visited.append((nrx,nry,nbx,nby))
                q.append((nrx,nry,nbx,nby,depth+1))
    print(0)

bfs()