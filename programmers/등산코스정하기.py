#TITLE: 등산코스 정하기 (https://school.programmers.co.kr/learn/courses/30/lessons/118669)
#LEVEL: 3
#TAG: kakao, dijkstra
#DATE: 20220921
#AUTHOR: squareyun

import heapq

def solution(n, paths, gates, summits):
    answer = []
    graph = [[] for i in range(n+1)]
    
    for i, j, w in paths:
        graph[i].append((j, w))
        graph[j].append((i, w))
        
    intensity = [float('inf')] * (n + 1)
    pq = []
    for start in gates:
        intensity[start] = 0
        pq.append((0, start))

    answer = []
    while pq:
        node_intensity, node = heapq.heappop(pq)

        # 이미 계산해 둔 intensity보다 더 큰 경우에는 볼 필요 없음
        if intensity[node] < node_intensity:
            continue
        
        # 산봉우리 도착시 완료
        if node in summits:
            answer.append([node, intensity[node]])
            continue
        
        for next_node, next_intensity in graph[node]:
            max_intensity = max(intensity[node], next_intensity)
            if max_intensity < intensity[next_node]: # 최소값 저장
                intensity[next_node] = max_intensity
                heapq.heappush(pq, (intensity[next_node], next_node))

    answer.sort(key=lambda x: (x[1], x[0]))
    return answer[0]

n = 6
paths=[[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
gates=[1,3]
summits=[5]
print(f'answer: {solution(n, paths, gates, summits)}')