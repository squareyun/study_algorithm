# TITLE: 기타줄 (https://www.acmicpc.net/problem/1049)
# LEVEL: Silver 4
# TAG: math, greedy
# DATE: 20220825
# AUTHOR: squareyun

n,m=map(int,input().split())
price=[]
for _ in range(m):
    price.append(list(map(int,input().split())))
package = sorted(price,key=lambda x:x[0])
solo = sorted(price,key=lambda x:x[1])

answer=0
if package[0][0] <= solo[0][1] * 6:
    d,m = divmod(n,6)
    answer = package[0][0] * d + solo[0][1] * m
    if package[0][0] < solo[0][1] * m:
        answer = package[0][0] * (d + 1)
else:
    answer = solo[0][1] * n
print(answer)