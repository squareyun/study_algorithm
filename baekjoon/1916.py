#TITLE: 최소비용 구하기 (https://www.acmicpc.net/problem/1916)
#LEVEL: G5
#TAG: dijkstra, graphs
#DATE: 20220927
#AUTHOR: squareyun

import heapq

n=int(input())
m=int(input())

graph=[[] for _ in range(n+1)]
distance=[float('inf')] * (n+1)

for _ in range(m):
    s,e,w=map(int,input().split())
    graph[s].append((e,w))

src,dst=map(int,input().split())

q=[]
heapq.heappush(q, (0, src))
distance[src] = 0
while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[dst])