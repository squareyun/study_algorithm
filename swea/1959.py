#TITLE: 두 개의 숫자열
#LEVEL: D2
#DATE: 20230102

T = int(input())

def solution(a, b):
    if len(a) > len(b):
        t = b
        b = a
        a = t
    
    answer = float('-inf')
    for i in range(0, len(b)-len(a)+1):
        temp = 0
        for j in range(len(a)):
            temp += b[i+j] * a[j]
        answer = max(answer, temp)

    return answer

for test_case in range(1, T + 1):
    n, m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    print(f'#{test_case} {solution(a, b)}')