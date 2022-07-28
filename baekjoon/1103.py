#게임(https://www.acmicpc.net/problem/1103)
import sys
sys.setrecursionlimit(10**6)

n,m=map(int,input().split())
map=[list(input()) for _ in range(n)]
dp=[[0]*m for _ in range(n)]
visited=[[False]*m for _ in range(n)]
answer=0

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def dfs(x, y, cnt):
    global answer
    answer=max(answer,cnt)
    w=int(map[x][y])
    for i in range(4):
        nx, ny = x+w*dx[i], y+w*dy[i]
        if nx>=0 and ny>=0 and nx<n and ny<m and map[nx][ny] != 'H' and cnt+1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                sys.exit(0)
            else:
                dp[nx][ny]=cnt+1
                visited[nx][ny]=True
                dfs(nx,ny,cnt+1)
                visited[nx][ny]=False
dfs(0,0,1)
print(answer)