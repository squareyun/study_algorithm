'''
UIUX디자이너
4 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 4
4 1 2 3 3
output: 3
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
event = dict()
for i in range(1, N+1):
    event[i] = 0

for i in range(M):
    a = list(map(int, input().split()))
    for j in a[1:]:
        event[j] += 1
answer = []
max = -1
for key in event.keys():
    i = event[key]
    if i == max:
        answer.append(key)
    if i > max:
        max = i
        answer = [key]
print(*answer[::-1])