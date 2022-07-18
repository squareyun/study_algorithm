s = input()
n = int(input())
a = []
for i in range(n):
    a.append(input())
dp = [-1] * (len(s) + 1)

def word(pos):
    if dp[pos] != -1: return dp[pos]

    if pos == len(s): return 1

    dp[pos] = 0
    for i in range(n):
        if s[pos:].startswith(a[i]):
            dp[pos] = max(dp[pos], word(pos + len(a[i])))
    return dp[pos]

print(word(0))