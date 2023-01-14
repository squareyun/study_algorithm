#TITLE: 랜선 자르기
#LEVEL: Silver 2
#TAG: binary search
#DATE: 20230114

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]
start = 1
end = max(lan)

while start <= end:
    mid = (start + end) // 2

    sum = 0
    for i in range(k):
        sum += lan[i] // mid

    if sum >= n:
        start = mid + 1
    else:
        end = mid - 1

print(end)