#TITLE: 나무 자르기
#LEVEL: Silver 2
#TAG: binary search
#DATE: 20230114

n, m = map(int, input().split())
tree = list(map(int, input().split()))
start = 0
end = max(tree) - 1

while start <= end:
    mid = (start + end) // 2

    get = 0
    for i in tree:
        if i > mid:
            get += i - mid
    
    if get >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)