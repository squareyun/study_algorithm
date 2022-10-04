#TITLE: 트리의 지름 (https://www.acmicpc.net/problem/1967)
#LEVEL: G4
#TAG: graphs, graph_traversal, trees
#DATE: 20221004
#AUTHOR: squareyun

from collections import deque
import sys
input=sys.stdin.readline
n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n-1):
    s,e,w = map(int,input().split())
    graph[s].append([w, e])
    graph[e].append([w, s])

def bfs(start):
    dp = [-1] * (n+1)
    q = deque()
    q.append(start)
    dp[start] = 0
    ret = [0, 0] # 이동 거리, 노드 번호

    while q:
        now = q.popleft()

        for weight, next_node in graph[now]:
            if dp[next_node] != -1:
                continue
            dp[next_node] = dp[now] + weight
            q.append(next_node)
            if ret[0] < dp[next_node]:
                ret = [dp[next_node], next_node]

    return ret

max_dist1, max_node1 = bfs(1)
max_dist2, max_node2 = bfs(max_node1)
print(max_dist2)