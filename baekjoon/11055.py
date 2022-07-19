n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

dp[0] = a[0]
for i in range(1, n):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += a[i]

print(max(dp))