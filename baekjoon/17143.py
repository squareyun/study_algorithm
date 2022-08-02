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
            nx,ny=r,c

            if d==1 or d==2:
                s=s%(2*R-2)
            elif d==3 or d==4:
                s=s%(2*C-2)

            for i in range(s):
                nx=nx+dx[d]
                ny=ny+dy[d]
                if nx < 1:
                    d=change(d)
                    nx+=2
                elif nx > R:
                    d=change(d)
                    nx-=2
                elif ny < 1:
                    d=change(d)
                    ny+=2
                elif ny > C:
                    d=change(d)
                    ny-=2

            if not tshark[nx][ny] or (z > tshark[nx][ny][2]):
                tshark[nx][ny] = [s,d,z]
    shark=tshark

for col in range(1,C+1): #열 개수만큼 반복
    catch(col)
    if col == C: break
    move()

print(answer)