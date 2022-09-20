# TITLE: 두 큐 합 같게 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/118667)
# LEVEL: 2
# TAG: kakao, deque
# DATE: 20220920
# AUTHOR: squareyun

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    answer = 0
    flag = False
    for _ in range(len(q1) * 3):
        if sum1 == sum2:
            flag = True
            break

        if sum1 > sum2:
            t = q1.popleft()
            q2.append(t)
            sum1 -= t
            sum2 += t
        else:
            t = q2.popleft()
            q1.append(t)
            sum1 += t
            sum2 -= t
        answer += 1
    if not flag:
        return -1
    return answer