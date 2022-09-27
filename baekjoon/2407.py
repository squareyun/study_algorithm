#TITLE: 조합 (https://www.acmicpc.net/problem/2407)
#LEVEL: S4
#TAG: combinatorics, math
#DATE: 20220927
#AUTHOR: squareyun

from math import factorial as f
n,m=map(int,input().split())
print(f(n)//(f(n-m)*f(m)))