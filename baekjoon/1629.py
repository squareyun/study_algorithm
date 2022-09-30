#TITLE: 곱셈 (https://www.acmicpc.net/problem/1629)
#LEVEL: S1
#TAG: math, divide_and_conquer
#DATE: 20220930
#AUTHOR: squareyun

def solve(a, b, c):
    if b == 1:
        return a % c
    elif b % 2 == 0:
        return (solve(a, b//2, c) ** 2) % c
    else:
        return ((solve(a, b//2, c) ** 2) * a) % c

a, b, c = map(int, input().split())
print(solve(a, b, c))