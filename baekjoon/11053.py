n = int(input())
a = list(map(int, input().split()))
dp = [0] * n

def sol(k):
    if k == 0: return 1
    if dp[k] != 0: return dp[k]

    dp[k] = 1
    for i in range(k-1, -1, -1):
        if a[i] < a[k]:
            dp[k] = max(dp[k], sol(i) + 1)
    
    return dp[k]

ret = 0
for i in range(n):
    ret = max(ret, sol(i))
print(ret)