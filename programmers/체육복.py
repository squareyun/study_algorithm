# TITLE: 체육복 (https://school.programmers.co.kr/learn/courses/30/lessons/42862)
# DATE: 20220803
# AUTHOR: squareyun
# TYPE: greedy

def solution(n, lost, reserve):
    answer = n
    lost = set(lost); reserve = set(reserve)

    for i in range(1, n+1):
        if i in lost and i in reserve:
            lost.remove(i)
            reserve.remove(i)

    for l in lost:
        if l-1 in reserve:
            reserve.remove(l-1)
        elif l+1 in reserve:
            reserve.remove(l+1)
        else:
            answer -= 1

    return answer