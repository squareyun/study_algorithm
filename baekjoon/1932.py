import sys

n = int(input())

nums = []
dp = [ [0] * i for i in range(1, n + 1) ]
for i in range(1, n + 1):
    temp = list(map(int, input().split()))
    nums.append(temp)

if n == 1:
    print(nums[0][0])
    sys.exit(0)
elif n == 2:
    print(max(nums[0][0] + nums[1][0], nums[0][0] + nums[1][1]))
    sys.exit(0)

dp[0][0] = nums[0][0]
dp[1][0] = nums[0][0] + nums[1][0]
dp[1][1] = nums[0][0] + nums[1][1]

for i in range(2, n):
    for j in range(i + 1):
        if j == 0:
            dp[i][j] = dp[i-1][j] + nums[i][j]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + nums[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1] + nums[i][j], dp[i-1][j] + nums[i][j])

print(max(dp[-1]))