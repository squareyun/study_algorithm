#TITLE: N과 M (5) (https://www.acmicpc.net/problem/15654)
#LEVEL: S3
#TAG: backtracking
#DATE: 20220927
#AUTHOR: squareyun

n,m=map(int,input().split())
a = list(map(int,input().split()))
a.sort() # for 사전순 출력
visited = [False] * (n)
answer = []

def dfs(depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(a[i])
            dfs(depth+1)
            answer.pop()
            visited[i] = False

dfs(0)