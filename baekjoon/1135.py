#뉴스 전하기(https://www.acmicpc.net/problem/1135)
n=int(input())
nums=list(map(int,input().split()))
tree=[[] for _ in range(n)]
for i in range(1, n):
    tree[nums[i]].append(i)

#dp[i]: i를 root로하는 subtree에 전달하는데 걸리는 시간
dp = [0]*n

def dfs(k):
    child_time = []
    for i in tree[k]:
        dfs(i) #리프노드까지 내려가기
        child_time.append(dp[i]) #자식들이 subtree에 전달하는데 걸리는 시간을 모아둠
    if not tree[k]:
        child_time.append(0)
    
    child_time.sort(reverse=True) #오래걸리는 순으로 먼저
    for i in range(len(child_time)):
        dp[k] = max(dp[k], child_time[i] + i + 1) #자식들에게 전파하는 시간의 최대값 + 1

dfs(0)
print(dp[0]-1) #root가 전파하는 시간 제외