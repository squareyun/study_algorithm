#TITLE: 달력 (https://www.acmicpc.net/problem/20207)
#LEVEL: Silver 1
#TAG: implementation, greedy
#DATE: 20220913
#REFERENCE: https://tmdrl5779.tistory.com/138

n=int(input())
calendar=[0]*366
for i in range(n):
    s,e=map(int,input().split())
    for j in range(s,e+1):
        calendar[j] += 1
answer=0
maxc=maxr=0
for i in range(366):
    if calendar[i] != 0:
        maxc = max(maxc, calendar[i])
        maxr += 1
    else:
        answer += maxc * maxr
        maxc=maxr=0
answer += maxc * maxr
print(answer)