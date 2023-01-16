#TITLE: 스택 수열
#LEVEL: Silver 2
#TAG: stack
#DATE: 20230116

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

answer = []
stack = []

now = 1
index = 0

while index != n:
    x = arr[index]

    if len(stack) == 0 or x > stack[-1]:
        stack.append(now)
        answer.append('+')
        now = now + 1
        continue

    if x == stack[-1]:
        stack.pop()
        answer.append('-')
        index += 1

    elif x < stack[-1]:
        answer = 'NO'
        break


if answer == 'NO':
    print(answer)
else:
    for i in answer:
        print(i)
