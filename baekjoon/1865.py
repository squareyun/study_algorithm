#TITLE: 웜홀 (https://www.acmicpc.net/problem/1865)
#LEVEL: G3
#TAG: bellman_ford, graphs
#DATE: 20221004
#AUTHOR: squareyun

import sys
input=sys.stdin.readline
INF = int(1e9)

def bellman_ford(start):
    dist = [INF] * (n + 1)
    dist[start] = 0

    # n-1 (vertex개수-1) 번 반복
    for i in range(n):
        for j in range(len(edges)):
            s, e, t = map(int,edges[j])
            
            if dist[e] > dist[s] + t:
                dist[e] = dist[s] + t
                if i == n-1: # n번째에도 존재한다면 음의 cycle 존재
                    return True
    return False

tc = int(input())
for _ in range(tc):
    n,m,w = map(int,input().split())
    edges=[]
    for _ in range(m):
        s,e,t=map(int,input().split())
        edges.append([s, e, t])
        edges.append([e, s, t])
    for _ in range(w):
        s,e,t=map(int,input().split())
        edges.append([s, e, -t])
    print('YES' if bellman_ford(1) else 'NO')