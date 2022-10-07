#TITLE: 병사 배치하기 (https://www.acmicpc.net/problem/18353)
#LEVEL: S2
#TAG: dp, lis
#DATE: 20221007
#AUTHOR: squareyun

n=int(input())
a=list(map(int,input().split()))
dp=[1]*n
for i in range(1, n):
    for j in range(i):
        if a[j] > a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(n-max(dp))