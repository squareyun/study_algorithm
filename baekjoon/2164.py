#TITLE: 카드2
#LEVEL: Silver 4
#TAG: queue
#DATE: 20230128

from collections import deque
n=int(input())
q=deque([])
for i in range(1,n+1):
    q.append(i)
while len(q) > 1:
    q.popleft()
    q.append(q.popleft())
print(q.pop())