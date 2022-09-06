# TITLE: 외벽 점검 (https://school.programmers.co.kr/learn/courses/30/lessons/60062)
# LEVEL: 3
# TAG: kakao, implementation
# DATE: 20220906
# REFERENCE: 이코테

from itertools import permutations

def solution(n, weak, dist):
    answer = len(dist) + 1
    length = len(weak)
    
    # 원형을 선형 형태로 변형
    for i in range(length):
        weak.append(weak[i] + n)
    
    for start in range(length): # 시작 지점
        for friends in list(permutations(dist, len(dist))):
            cnt = 1
            pos = weak[start] + friends[cnt - 1] # 해당 친구가 점검 가능한 마지막 위치
            
            for idx in range(start, start + length):
                if pos < weak[idx]: # 점검할 수 있는 범위를 벗어남
                    cnt += 1 # 새친구 투입
                    if cnt > len(dist):
                        break
                    pos = weak[idx] + friends[cnt - 1]
            answer = min(answer, cnt)
    
    if answer > len(dist):
        return -1
    
    return answer