#TITLE: 무지의 먹방 라이브 (https://school.programmers.co.kr/learn/courses/30/lessons/42891)
#LEVEL: 4
#TAG: greedy
#DATE: 20221007
#AUTHOR: squareyun
#REFERENCE: 이것이 코딩테스트다

import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    foods = []
    for i in range(len(food_times)):
        heapq.heappush(foods, (food_times[i], i+1))
    
    count = 0 #지금까지 걸린 시간
    prev = 0 #방금 먹어치운 양
    length = len(food_times)
    
    while count + (foods[0][0] - prev) * length <= k:
        now = heapq.heappop(foods)[0]
        count += (now - prev) * length
        length -= 1
        prev = now
    
    foods.sort(key=lambda x:x[1])
    return foods[(k - count) % length][1]