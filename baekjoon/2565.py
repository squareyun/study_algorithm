#TITLE: 전깃줄 (https://www.acmicpc.net/problem/2565)
#LEVEL: G5
#TAG: dp, lis
#DATE: 20221007
#AUTHOR: squareyun

n=int(input())
pos=[]
for _ in range(n):
    pos.append(list(map(int,input().split())))

pos.sort()

dp = [1] * n
for i in range(n):
    for j in range(i):
        if pos[i][1] > pos[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n-max(dp))