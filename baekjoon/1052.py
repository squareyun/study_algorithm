#TITLE: 물병 (https://www.acmicpc.net/problem/1052)
#LEVEL: Silver 1
#TAG: greedy, implementation
#DATE: 20220909
#AUTHOR: squareyun

n,k=map(int,input().split())
answer=0

while bin(n).count('1') > k:
    n += 1
    answer += 1

print(answer)