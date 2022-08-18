# TITLE: 백양로 브레이크 (https://www.acmicpc.net/problem/11562)
# LEVEL: Gold 3
# TAG: graph, floyd warshall
# DATE: 20220818
# AUTHOR: squareyun

INF=int(1e9)
n,m=map(int,input().split())
graph=[[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    graph[i][i]=0

for i in range(m):
    u,v,b=map(int,input().split())
    if b:
        graph[u][v]=0
        graph[v][u]=0
    else:
        graph[u][v]=0
        graph[v][u]=1 #양방향을 위한 통로 비용

for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

k=int(input())
for i in range(k):
    s,e=map(int,input().split())
    print(graph[s][e])