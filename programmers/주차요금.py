# TITLE: 주차 요금 계산 (https://school.programmers.co.kr/learn/courses/30/lessons/92341)
# LEVEL: 2
# TAG: kakao
# DATE: 20220907
# AUTHOR: squareyun

import math
def solution(fees, records):
    answer = []
    d = dict()
    for record in records:
        time, num, state = record.split(" ")
        hh, mm = time.split(":")
        if num not in d:
            d[num] = [int(hh) * 60 + int(mm)]
        else:
            d[num].append(int(hh) * 60 + int(mm))
    
    for k, v in d.items():
        t = 0
        long = 0
        for i in range(0, len(v), 2):
            n1 = v[i]
            try:
                n2 = v[i+1]
            except:
                n2 = 23 * 60 + 59
            long += (n2 - n1)
        t += fees[1]
        if long > fees[0]:
            t += math.ceil(((long - fees[0]) / fees[2])) * fees[3]
        answer.append((k, t))
    
    answer.sort(key=lambda x: x[0])
    ret = [x[1] for x in answer]
    
    return ret