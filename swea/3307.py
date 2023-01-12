#TITLE: 최장 증가 부분 수열
#LEVEL: D3
#DATE: 20230112

T = int(input())
 
def solution(n, arr):
    dp = [1] * n
 
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
 
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))
    print(f'#{test_case} {solution(n, arr)}')