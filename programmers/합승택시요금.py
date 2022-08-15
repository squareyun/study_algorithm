# TITLE: 합승 택시 요금 (https://school.programmers.co.kr/learn/courses/30/lessons/72413)
# TAG: graph, floyd warshall, dp, kakao
# DATE: 20220815
# AUTHOR: squareyun

def solution(n, s, a, b, fares):
    INF = int(1e9)
    answer = INF
    graph = [[INF] * (n+1) for _ in range(n+1)]
    
    for i in range(1,n+1):
        for j in range(1, n+1):
            if i == j:
                graph[i][j] = 0
    
    for i, j, k in fares:
        graph[i][j] = k
        graph[j][i] = k
        
    #최단경로 그래프 구성
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    
    for k in range(1, n+1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b]) #핵심
        
    return answer