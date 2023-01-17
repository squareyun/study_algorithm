#TITLE: 프린터 큐
#LEVEL: Silver 3
#TAG: queue, implementation
#DATE: 20230117

from collections import deque

test_case = int(input())

for _ in range(test_case):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque([])
    for i in range(len(arr)):
        q.append((arr[i], i))
    
    cnt = 1

    while len(q) > 0:
        weight, cur = q.popleft()

        canPrint = True
        for i in range(len(q)):
            if weight < q[i][0]:
                q.append((weight, cur))
                canPrint = False
                break
        
        if canPrint:
            if cur == m: break
            else: cnt += 1

    print(cnt)