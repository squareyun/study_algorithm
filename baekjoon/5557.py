# TITLE: 1학년 (https://www.acmicpc.net/problem/5557)
# LEVEL: Gold 5
# TAG: dp
# DATE: 20220819
# AUTHOR: squareyun

n=int(input())
num=list(map(int,input().split()))
dp = [[0] * 21 for _ in range(n)]
# dp[idx][현재계산결과] = 경우의 수
dp[0][num[0]] += 1
for i in range(1, n-1):
    for j in range(21):
        if dp[i-1][j]:
            if j + num[i] <= 20:
                dp[i][j + num[i]] += dp[i - 1][j]
            if j - num[i] >= 0:
                dp[i][j - num[i]] += dp[i - 1][j]
print(dp[n-2][num[n-1]])