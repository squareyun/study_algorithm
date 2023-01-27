#TITLE: 수 찾기
#LEVEL: Silver 4
#TAG: binary_search
#DATE: 20230127

n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
a.sort()

def solve(k):
    l, r = 0, n
    
    while l < r:
        mid = (l+r)//2
        if a[mid] == k:
            return k
        elif a[mid] > k:
            r = mid
        else:
            l = mid + 1
    return -1

for i in b:
    if solve(i) == -1:
        print(0)
    else:
        print(1)