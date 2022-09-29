#TITLE: 트리의 지름 (https://www.acmicpc.net/problem/1167)
#LEVEL: G2
#TAG: graph_traversal, tree
#DATE: 20220929
#AUTHOR: squareyun
#REFERENCE: https://bit.ly/3E4cOjI

from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
graph = [ [] * (v+1) for _ in range(v+1)]
for _ in range(v):
    t = list(map(int, input().split()))
    for j in range(1, len(t)-1, 2):
        graph[t[0]].append((t[j], t[j+1]))

def bfs(start):
    dp = [-1] * (v+1)
    q = deque()
    q.append(start)
    dp[start] = 0
    ret = [0, 0] # 이동 거리, 노드 번호

    while q:
        cur = q.popleft()
        for next, w in graph[cur]:
            if dp[next] == -1:
                dp[next] = dp[cur] + w
                q.append(next)
                if ret[0] < dp[next]:
                    ret = dp[next], next
    
    return ret

# 트리의 지름을 구하는 공식 (임의의 정점에서 가장 긴 정점을 찾고, 그 정점에서 가장 긴 거리를 찾으면 됨)
distance, node = bfs(1)
distance, node = bfs(node)
print(distance)
