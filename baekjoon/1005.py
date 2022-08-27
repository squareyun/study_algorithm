# TITLE: ACM Craft (https://www.acmicpc.net/problem/1005)
# LEVEL: Gold 3
# TAG: dp, graph, topological_sorting
# DATE: 20220827
# AUTHOR: squareyun

import sys
from collections import deque
input = sys.stdin.readline
t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    D=[0] + list(map(int,input().split()))
    indegree=[0] * (n+1)
    graph=[[] for _ in range(n+1)]
    DP=[0 for _ in range(n+1)]
    for _ in range(k):
        a,b=map(int,input().split())
        graph[a].append(b)
        indegree[b] += 1
    w=int(input())
    
    progress=[[] for _ in range(n+1)]
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)
            DP[i] = D[i]
    while q:
        now=q.popleft()
        for i in graph[now]:
            DP[i] = max(DP[i], DP[now] + D[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    print(DP[w])