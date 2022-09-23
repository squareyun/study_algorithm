#TITLE: N과 M (2) (https://www.acmicpc.net/problem/15650)
#LEVEL: S3
#TAG: backtracking
#DATE: 20220923
#AUTHOR: squareyun

n,m=map(int,input().split())
visited=[False] * (n+1)
answer = []

def dfs(num, depth):
    if depth == m:
        t = ''
        for i in answer:
            t += str(i) + ' '
        print(t)
        return
    
    for i in range(num, n+1):
        if not visited[i]:
            answer.append(i)
            visited[i] = True
            dfs(i+1, depth+1)
            visited[i] = False
            answer.pop()

dfs(1, 0)