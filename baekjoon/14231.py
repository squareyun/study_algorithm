#TITLE: 박스 포장
#LEVEL: Silver 2
#TAG: dp
#DATE: 20230118

n = int(input())
arr = list(map(int, input().split()))
brr = [1] * n

for i in range(n):
    for j in range(i+1):
        if arr[i] > arr[j]:
            brr[i] = max(brr[i], brr[j] + 1)

print(max(brr))