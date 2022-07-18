# 직관적인 풀이
s = input()
n = int(input())
a = [input() for i in range(n)]
dp = [False for _ in range(len(s) + 1)]

dp[0] = True
for i in range(len(s)):
    if not dp[i]:
        continue

    for t in a:
        if s[i:i+len(t)] == t:
            dp[i+len(t)] = True
print(int(dp[len(s)]))

# 다른 풀이
# s = input()
# n = int(input())
# a = []
# for i in range(n):
#     a.append(input())
# dp = [-1] * (len(s) + 1)

# def word(pos):
#     if dp[pos] != -1: return dp[pos]

#     if pos == len(s): return 1

#     dp[pos] = 0
#     for i in range(n):
#         if s[pos:].startswith(a[i]):
#             dp[pos] = max(dp[pos], word(pos + len(a[i])))
#     return dp[pos]

# print(word(0))