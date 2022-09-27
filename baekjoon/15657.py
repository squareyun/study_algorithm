#TITLE: N과 M (8) (https://www.acmicpc.net/problem/15657)
#LEVEL: S3
#TAG: backtracking
#DATE: 20220927
#AUTHOR: squareyun

n,m=map(int,input().split())
a = list(map(int,input().split()))
a.sort() # for 사전순 출력
answer = []

def dfs(idx, depth):
    if depth == m:
        print(' '.join(map(str, answer)))
        return
    
    for i in range(idx, n):
        answer.append(a[i])
        dfs(i, depth + 1)
        answer.pop()

dfs(0, 0)