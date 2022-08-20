# TITLE: 제곱 ㄴㄴ 수 (https://www.acmicpc.net/problem/1016)
# LEVEL: Gold 1
# TAG: math, number_tehory, primality_test, sieve
# DATE: 20220820
# AUTHOR: squareyun
# REFERENCE: https://bit.ly/3T1zPc3

n,m=map(int,input().split())
sieve = [1] * (m - n + 1)
for k in range(2, int(m ** 0.5) + 1):
    s = k * k
    i = 0 if n % s == 0 else s - (n % s)
    for j in range(i, len(sieve), s):
        sieve[j] = 0
print(sum(sieve))