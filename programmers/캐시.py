# TITLE: 캐시 (https://school.programmers.co.kr/learn/courses/30/lessons/17680#)
# LEVEL: 2
# TAG: kakao, lru
# DATE: 20220901
# AUTHOR: squareyun

import heapq

def solution(cacheSize, cities):
    answer = 0
    heap=[]
    check=set()
    maxprio=0

    if cacheSize < 1:
        return 5*len(cities)
    
    for city in cities:
        city = city.lower()
        if city in check:
            answer += 1
            for i in range(len(heap)):
                if heap[i][1] == city:
                    t=heap[i]
                    maxprio += 1
                    heap[i] = (maxprio, t[1])
                    heapq.heapify(heap)
                    break
        else:
            if len(check) == cacheSize:
                t=heapq.heappop(heap)
                check.remove(t[1])
            maxprio += 1
            heapq.heappush(heap, (maxprio, city))
            check.add(city)
            answer += 5
        
    return answer