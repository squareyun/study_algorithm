#TITLE: 추월 (https://www.acmicpc.net/problem/2002)
#LEVEL: Silver 1
#TAG: implementation, hash_set, string
#DATE: 20220913
#AUTHOR: squareyun

n=int(input())
inList=[input() for _ in range(n)]
outList=[input() for _ in range(n)]
answer=set()
for i in range(n):
    a = set(inList[:i])
    bIdx = outList.index(inList[i])
    b = set(outList[:bIdx])
    t = b.difference(a)
    answer = answer.union(t)
print(len(answer))