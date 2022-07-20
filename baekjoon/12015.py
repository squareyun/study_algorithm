import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
lis = [a[0]]
for i in range(1, n):
    if a[i] > lis[-1]:
        lis.append(a[i])
    else:
        # 이분탐색
        l = 0
        h = len(lis) - 1
        while l < h:
            m = (l + h) // 2
            if lis[m] < a[i]:
                l = m + 1
            else:
                h = m
        lis[l] = a[i]
print(len(lis))