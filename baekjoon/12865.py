n, k = map(int, input().split())

weights = [-1]
values = [-1]
for i in range(n):
    w, v = map(int, input().split())
    weights.append(w)
    values.append(v)

dp = [[0] * (k + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for w in range(1, k + 1):
        if weights[i] <= w:
            dp[i][w] = max(dp[i-1][w], values[i] + dp[i-1][w-weights[i]])
        else:
            dp[i][w] = dp[i-1][w]

print(dp[n][k])