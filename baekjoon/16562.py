# TITLE: 친구비 (https://www.acmicpc.net/problem/16562)
# LEVEL: Gold 4
# TAG: data_structure, disjoint_set, graph
# DATE: 20220826
# AUTHOR: squareyun

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
n,m,k=map(int,input().split())
root=[i for i in range(n+1)]
arr=list(map(int,input().split()))
def find(x):
    if root[x] != x:
        root[x] = find(root[x])
    return root[x]

def union(x, y):
    rootX = find(x)
    rootY = find(y)
    if rootX != rootY:
        if arr[rootX-1] <= arr[rootY-1]:
            root[rootY] = rootX
        else:
            root[rootX] = rootY

for _ in range(m):
    a,b=map(int,input().split())
    union(a,b)

answer = 0
for i in range(1,n+1):
    if i == root[i]:
        answer += arr[i-1]
print('Oh no') if answer > k else print(answer)