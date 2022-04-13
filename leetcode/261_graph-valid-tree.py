# 채점 하지 않은 코드임.

def is_valid_tree(n, edges):
    root = [i for i in range(n)]

    def find(x):
        if root[x] != x:
            root[x] = find(root[x])
        return root[x]

    def union(x, y):
        rootX = find(x)
        rootY = find(y)
        if rootX != rootY:
            root[rootY] = rootX
    
    for e1, e2 in edges:
        if find(e1) == find(e2):
            return False    # 차례대로 노드를 연결하는 과정에서, 부모 노드가 동일하다면 사이클이 발생한 것
        else:
            union(e1, e2)
    return True