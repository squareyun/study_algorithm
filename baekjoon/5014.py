#TITLE: 스타트링크 (https://www.acmicpc.net/problem/5014)
#LEVEL: G5
#TAG: graphs, graph_traversal, bfs
#DATE: 20220922
#AUTHOR: squareyun

from collections import deque

f,s,g,u,d=map(int,input().split())
dp = [0] * (f+1)

def bfs():
    q = deque([s])
    while q:
        now = q.popleft()
        if now == g:
            return dp[g]

        for i in [now + u, now - d]:
            if i == now: #반례: 1000000 1000000 1 0 1 -> 999999
                continue
            if 1 <= i <= f and dp[i] == 0:
                dp[i] = dp[now] + 1
                q.append(i)
    return 'use the stairs'

print(bfs())