#TITLE: N과 M (1) (https://www.acmicpc.net/problem/15649)
#LEVEL: S3
#TAG: backtracking
#DATE: 20220923
#AUTHOR: squareyun

n,m=map(int,input().split())
visited=[False] * (n+1)
answer = [0] * m

def dfs(k):
    if k == m:
        t = ''
        for i in answer:
            t += str(i) + ' '
        print(t)
        return
    
    for i in range(1, n+1):
        if not visited[i]:
            answer[k] = i
            visited[i] = True
            dfs(k+1)
            visited[i] = False

dfs(0)