# TITLE: k진수에서 소수 개수 구하기 (https://school.programmers.co.kr/learn/courses/30/lessons/92335)
# LEVEL: 2
# TAG: kakao, prime
# DATE: 20220907
# AUTHOR: squareyun

import math

def is_prime(n):
    if n == 1: return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    base = ''
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)
    num = base[::-1]
    
    sp = str(num).split("0")
    
    for s in sp:
        if s == '': continue
        if is_prime(int(s)):
            answer += 1
    
    return answer