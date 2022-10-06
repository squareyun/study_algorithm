#TITLE: 트리 순회 (https://www.acmicpc.net/problem/1991)
#LEVEL: S1
#TAG: trees, recursion
#DATE: 20221006
#AUTHOR: squareyun

n=int(input())
tree=dict()
for _ in range(n):
    root, l, r = input().split()
    tree[root] = (l, r)

def preorder(v):
    if v == '.':
        return
    
    print(v, end="")
    preorder(tree[v][0])
    preorder(tree[v][1])

def inorder(v):
    if v == '.':
        return
    
    inorder(tree[v][0])
    print(v, end="")
    inorder(tree[v][1])

def postorder(v):
    if v == '.':
        return
    
    postorder(tree[v][0])
    postorder(tree[v][1])
    print(v, end="")

preorder('A')
print()
inorder('A')
print()
postorder('A')