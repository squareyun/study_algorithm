# Anti-parallel edges 탐색 및 수정하는 함수
def antiParallel(graph):
    for e1 in range(len(graph)):
        for e2 in range(len(graph[e1])):
            if e1 == e2: continue
            ew1 = graph[e1][e2]
            ew2 = graph[e2][e1]
            if ew1 != 0 and ew2 != 0:
                if ew1 > ew2:
                    graph[e1][e2] = ew1 - ew2
                    graph[e2][e1] = 0
                else:
                    graph[e2][e1] = ew2 - ew1
                    graph[e1][e2] = 0
    return graph

def bfsRemain(capacity):
    visited = [0] * len(capacity)
    q = []
    visited[0] = 1
    q.append(0)
    ret = set()

    while len(q) != 0:
        u = q.pop(0)
        for v in range(len(capacity)):
            if visited[v] != 1 and capacity[u][v] > 0:
                q.append(v)
                visited[v] = 1
            elif capacity[u][v] <= 0:
                ret.add(u)
    
    return ret
        

# source to sink 경로가 residual network에 존재하는지 BFS 탐색
def bfsNetwork(capacity, parent):
    visited = [0] * len(capacity)
    q = []
    visited[0] = 1
    q.append(0)

    while len(q) != 0:
        u = q.pop(0)
        for v in range(len(capacity[u])):
            if visited[v] != 1 and capacity[u][v] > 0:
                q.append(v)
                parent[v] = u
                visited[v] = 1
                if v == len(capacity) - 1: # Path를 찾았다는 의미
                    return True

    return False

import copy

def fordFulkerson(graph):
    capacity = copy.deepcopy(graph)
    source = 0 # 출발지
    sink = len(capacity) - 1 # 목적지
    total_flow = 0
    parent = [-1] * len(capacity) # 경로의 부모 노드를 저장

    while bfsNetwork(capacity, parent): # source to sink 경로가 residual network에 존재할 때 반복
        cf = float('inf')
        t = sink
        while t != source:
            cf = min(cf, capacity[parent[t]][t]) # 경로 상의 최소값 탐색
            t = parent[t]

        total_flow += cf
        
        t = sink
        while t != source:
            capacity[t][parent[t]] += cf
            capacity[parent[t]][t] -= cf
            t = parent[t]
    
    print(total_flow)

    # min-cut 찾기
    # 잔여 용량이 있는 간선을 통해 갈 수 있는 노드 탐색
    remainNodes =  bfsRemain(capacity)
    mincut = []

    # 기존 그래프에서 그 노드중 갈 수 없는 마지막 노드와 연결된 간선 탐색
    for i in remainNodes:
        for j in range(len(graph[i])):
            if capacity[i][j] <= 0 and graph[i][j] > 0:
                mincut.append([i, j])
    
    print(mincut)

def maxPossibleFlow(graph):
    graph = antiParallel(graph)
    fordFulkerson(graph)

maxPossibleFlow([[0, 16, 13, 0, 0, 0],
	        [0, 0, 10, 12, 0, 0],
	        [0, 4, 0, 0, 14, 0],
	        [0, 0, 9, 0, 0, 20],
	        [0, 0, 0, 7, 0, 4],
	        [0, 0, 0, 0, 0, 0]])
