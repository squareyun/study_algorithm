# TITLE: 집합의 표현 (https://www.acmicpc.net/problem/1717)
# LEVEL: Gold 4
# TAG: data_structure, disjoint_set
# DATE: 20220826
# AUTHOR: squareyun

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m=map(int,input().split())
root = [i for i in range(n+1)]

def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX < rootY:
        root[rootY] = rootX
    else:
        root[rootX] = rootY

for _ in range(m):
    op,a,b=map(int,input().split())
    if op:
        print('YES') if find(a) == find(b) else print('NO')
    else:
        union(a, b)