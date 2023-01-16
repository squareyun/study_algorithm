#TITLE: 좌표 압축
#LEVEL: Silver 2
#TAG: sorting
#DATE: 20230116

import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
brr = sorted(list(set(arr)))

dic = dict()
for i in range(len(brr)):
    dic[brr[i]] = i

for i in range(n):
    print(dic[arr[i]], end=' ')