#타일링
dp=[0]*251
dp[0]=1 #둘 수 없는 것도 하나의 방법
dp[1]=1
dp[2]=3

def solve(n):
    if dp[n] != 0: return dp[n]
    for i in range(3, n+1):
        if dp[i] != 0: continue
        dp[i] = dp[i-1] + dp[i-2]*2
    return dp[n]

while True:
    try:
        print(solve(int(input())))
    except:
        break