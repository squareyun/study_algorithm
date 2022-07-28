#합분해(https://www.acmicpc.net/problem/2225)
n,k=map(int,input().split())
dp=[[0]*(k+1) for _ in range(n+1)]
for j in range(1,k+1):
    dp[1][j]=j
for i in range(2,n+1):
    dp[i][1] = i
    for j in range(1,k+1):
        if j == 2: dp[i][j] = i+1
        else: dp[i][j] = (dp[i-1][j] + dp[i][j-1])%1000000000
print(dp[n][k])