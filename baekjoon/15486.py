#TITLE: 퇴사 2
#LEVEL: Gold 5
#TAG: dp
#DATE: 20230126

import sys
input = sys.stdin.readline
n = int(input())
t = [0] * (n+1)
p = [0] * (n+1)
dp = [0] * (n+1)

for i in range(n):
    t[i], p[i] = map(int, input().split())

maxV = 0
for i in range(n):
    dp[i + 1] = max(dp[i], dp[i+1]) # i일에 일을 수행 안하는 것이 더 좋을 수도 있다.

    if i + t[i] > n:
        continue

    dp[i + t[i]] = max(dp[i + t[i]], dp[i] + p[i])

print(dp[n])