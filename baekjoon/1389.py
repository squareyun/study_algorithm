#TITLE: 케빈 베이컨의 6단계 법칙 (https://www.acmicpc.net/problem/1389)
#LEVEL: S1
#TAG: graphs, floyd_warshall

import sys
input=sys.stdin.readline
N, M = map(int,input().split())
INF = int(1e9)
graph = [[INF] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            graph[i][j] = 0

for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = []
for i in range(1, N+1):
    result.append(sum(graph[i][1:]))
print(result.index(min(result)) + 1)
