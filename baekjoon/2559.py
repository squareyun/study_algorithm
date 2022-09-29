#TITLE: 수열 (https://www.acmicpc.net/problem/2559)
#LEVEL: S3
#TAG: prefix_sum
#DATE: 20220929
#AUTHOR: squareyun

n,k=map(int,input().split())
a = [0] + list(map(int,input().split()))

for i in range(1, n+1):
    a[i] = a[i-1] + a[i]

answer = float('-inf')
for i in range(k, n+1):
    answer = max(answer, a[i] - a[i-k])
print(answer)