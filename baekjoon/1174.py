# TITLE: 줄어드는 수 (https://www.acmicpc.net/problem/1174)
# LEVEL: Gold 5
# TAG: backtracking, bruteforce
# DATE: 20220829
# AUTHOR: squareyun
# REFERENCE: https://deok2kim.tistory.com/322

n=int(input())
if n > 1023:
    print(-1)
    exit(0)

def make(cur):
    answer.append(int(cur))
    for i in range(int(cur[-1])):
        make(cur + str(i))

answer = []
for i in range(10):
    make(str(i))
answer.sort()
print(answer[n-1])