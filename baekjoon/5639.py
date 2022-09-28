#TITLE: 이진 검색 트리 (https://www.acmicpc.net/problem/5639)
#LEVEL: G4
#TAG: graphs, graph_traversal, recursion, trees
#DATE: 20220928
#AUTHOR: squareyun

import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
pre=[]
while True:
    try:
        pre.append(int(input()))
    except:
        break

def postorder(a):
    if len(a) <= 1:
        return a
    
    for i in range(1, len(a)):
        if a[0] < a[i]:
            return postorder(a[1:i]) + postorder(a[i:]) + [a[0]]
    
    return postorder(a[1:]) + [a[0]]

post = postorder(pre)
for p in post:
    print(p)