# TITLE: 공항 (https://www.acmicpc.net/problem/10775)
# LEVEL: Gold 2
# TAG: data_structure, disjoint_set, greedy
# DATE: 20220831
# AUTHOR: squareyun

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

g=int(input())
p=int(input())
root = [i for i in range(g+1)]
planes=[int(input()) for _ in range(p)]

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

answer = 0
for plane in planes:
    x = find(plane)
    if x == 0:
        break
    union(x, x-1)
    answer+=1
print(answer)