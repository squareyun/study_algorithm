# 채점 하지 않은 코드임.

def num_of_connected_component(n, edges):
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
        union(e1, e2)
    
    my_set = set(root) # 중복 루트인 경우를 제외해서 집합 만들기
    return len(my_set)
    
