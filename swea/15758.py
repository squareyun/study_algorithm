#TITLE: 무한 문자열 (https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AYP5JmsqcngDFATW)
#LEVEL: D2

def solution(s, t):
    if s * len(t) == t * len(s):
        return "yes"
    return "no"

T = int(input())
for test_case in range(1, T + 1):
    s, t = input().split()
    result = solution(s, t)
    print(f'#{test_case} {result}')