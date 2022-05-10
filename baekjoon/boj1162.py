import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

n, m, k = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [[INF] * (k+1) for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

q = []
heapq.heappush(q, (0, 1, 0)) # weight, source, 도로포장횟수
distance[1][0] = 0
while q:
    dist, now, count = heapq.heappop(q)

    if distance[now][count] < dist:
        continue

    for next, weight in graph[now]:
        cost = dist + weight
        # 포장하지 않을 때
        if cost < distance[next][count]:
            distance[next][count] = cost
            heapq.heappush(q, (cost, next, count))
        # 포장할 때
        if count < k and dist < distance[next][count + 1]:
            distance[next][count + 1] = dist
            heapq.heappush(q, (dist, next, count + 1))

print(min(distance[n]))