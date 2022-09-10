#TITLE: 치킨 배달 (https://www.acmicpc.net/problem/15686)
#LEVEL: Gold 5
#TAG: implementation, bruteforce
#DATE: 20220910
#AUTHOR: squareyun

from itertools import combinations
n,m=map(int,input().split())
city=[[0]*(n+1)]
homes=[]
chickens=[]

for i in range(1,n+1):
    t = [0] + list(map(int,input().split()))
    city.append(t)
    for j in range(1,len(t)):
        if t[j] == 1:
            homes.append([i, j])
        elif t[j] == 2:
            chickens.append([i, j])

def calculate(homes, chickens):
    global answer
    chickenDist = 0

    for h in homes:
        dist = 987654321
        for c in chickens:
            temp = abs(h[0] - c[0]) + abs(h[1] - c[1])
            dist = min(dist, temp)
        chickenDist += dist

    answer = min(chickenDist, answer)

answer = 987654321
for comb in combinations(chickens, m):
    calculate(homes, list(comb))
print(answer)
