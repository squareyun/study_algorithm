#TITLE: N과 M (9) (https://www.acmicpc.net/problem/15663)
#LEVEL: S2
#TAG: backtracking
#DATE: 20220927
#AUTHOR: squareyun

n,m=map(int,input().split())
a = list(map(int,input().split()))
a.sort() # for 사전순 출력
answer = []
ret = set()
visited = [False] * n

def dfs(depth):
    if depth == m:
        ret.add(tuple(answer))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            answer.append(a[i])
            dfs(depth + 1)
            answer.pop()
            visited[i] = False

dfs(0)
for a in sorted(ret):
    print(*a)

# ret = sorted(list(ret))
# for a in ret:
#     print(' '.join(map(str, a)))