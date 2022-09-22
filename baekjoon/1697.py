#TITLE: 숨바꼭질 (https://www.acmicpc.net/problem/1697)
#LEVEL: S1
#TAG: graphs, graph_traversal, bfs
#DATE: 20220922
#AUTHOR: squareyun

from collections import deque

n,k=map(int,input().split())
dp = [0] * 100001

def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            return
        possible = [now-1, now+1, now*2]
        for p in possible:
            if 0 <= p < 100001 and dp[p] == 0:
                q.append(p)
                dp[p] = dp[now] + 1

bfs()
print(dp[k])