# 낚시왕 (https://www.acmicpc.net/problem/17143)
import sys
R,C,m=map(int,input().split())
shark=[[[] for _ in range(C+1)] for _ in range(R+1)]
for _ in range(m):
    r,c,s,d,z=map(int,sys.stdin.readline().split())
    shark[r][c]=[s,d,z]
dx=[0,-1,1,0,0] #위,아래,오른쪽,왼쪽
dy=[0,0,0,1,-1]
answer=0

def change(d):
    if d == 1: return 2
    elif d == 2: return 1
    elif d == 3: return 4
    elif d == 4: return 3

def catch(col):
    global answer
    for i in range(1,R+1):
        if shark[i][col]:
            answer += shark[i][col][2]
            shark[i][col] = []
            return

def move():
    global shark
    tshark=[[[] for _ in range(C+1)] for _ in range(R+1)]
    for r in range(1,R+1):
        for c in range(1,C+1):
            if not shark[r][c]: continue
            sh=shark[r][c]
            s,d,z=sh[0],sh[1],sh[2]
            nx=r+s*dx[d]
            ny=c+s*dy[d]
            if nx < 1 or ny < 1 or nx > R or ny > C:
                if d == 1:
                    t = s - (r-1)
                    dir,move=divmod(t,(R-1))
                    if r != 1: d = change(d)
                    if dir % 2 == 0:
                        nx=1+move
                        if dir != 0 :
                            d = change(d)
                    else:
                        nx=R-move
                        if move != 0:
                            d = change(d)
                elif d == 2:
                    t = s - (R-r)
                    dir,move=divmod(t,(R-1))
                    if r != R: d = change(d)
                    if dir % 2 == 0:
                        nx=R-move
                        if dir != 0 :
                            d = change(d)
                    else:
                        nx=1+move
                        if move != 0:
                            d = change(d)
                elif d == 3:
                    t = s - (C-c)
                    dir,move=divmod(t,(C-1))
                    if c != C: d = change(d)
                    if dir % 2 == 0:
                        ny=C-move
                        if dir != 0 :
                            d = change(d)
                    else:
                        ny=1+move
                        if move != 0:
                            d = change(d)
                elif d == 4:
                    t = s - (c-1)
                    dir,move=divmod(t,(C-1))
                    if c != 1: d = change(d)
                    if dir % 2 == 0:
                        ny=1+move
                        if dir != 0 :
                            d = change(d)
                    else:
                        ny=C-move
                        if move != 0:
                            d = change(d)

            if not tshark[nx][ny] or (z > tshark[nx][ny][2]):
                tshark[nx][ny] = [s,d,z]
    shark=tshark

for col in range(1,C+1): #열 개수만큼 반복
    catch(col)
    if col == C: break
    move()

print(answer)