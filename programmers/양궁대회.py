#TITLE: 양궁대회 (https://school.programmers.co.kr/learn/courses/30/lessons/92342)
#LEVEL: 2
#TAG: kakao, simulation, bruteforce
#DATE: 20220908
#AUTHOR: squareyun
#REFERENCE: https://bit.ly/3cU0lE8

from itertools import combinations_with_replacement as cwr

def solution(n, info):
    # ret[0..10]: 10-i점에서 라이언이 맞힌 화살의 수, ret[11]: 점수 차이
    ret = [-1] * 12

    for comb in cwr(range(11), n):
        arrow = [0] * 12
        ryanScore = apeachScore = 0
        for i in comb:
            arrow[i] += 1
        for i in range(11):
            if arrow[i] > info[i]:
                ryanScore += (10 - i)
            elif info[i] != 0:
                apeachScore += (10 - i)
        if ryanScore <= apeachScore:
            continue
        arrow[11] = ryanScore - apeachScore
        if arrow[::-1] > ret[::-1]:
            ret = arrow[:]
    if ret[0] == -1:
        return [-1]
    return ret[:-1]