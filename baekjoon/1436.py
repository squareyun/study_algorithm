#TITLE: 영화감독 숌 (https://www.acmicpc.net/problem/1436)
#LEVEL: S5
#TAG: brute-force
#DATE: 20221008
#AUTHOR: squareyun

n=int(input())
cnt=1
num=666
while cnt != n:
    num += 1
    if '666' in str(num):
        cnt += 1
print(num)