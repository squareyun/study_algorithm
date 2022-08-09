# TITLE: 하노이의 탑 (https://school.programmers.co.kr/learn/courses/30/lessons/12946?language=python3)
# TAG: recursion
# DATE: 20220809
# AUTHOR: squareyun

answer = []
def hanoi(n, start, dest, temp):
    global answer

    if n <= 1:
        answer.append([start, dest])
        return

    hanoi(n-1, start, temp, dest)
    answer.append([start, dest])
    hanoi(n-1, temp, dest, start)

def solution(n):
    hanoi(n, 1, 3, 2)
    return answer