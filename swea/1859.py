#TITLE: 백만 장자 프로젝트 (https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5LrsUaDxcDFAXc&categoryId=AV5LrsUaDxcDFAXc&categoryType=CODE&problemTitle=1859&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1)
#LEVEL: D2
#DATE: 20221109
#AUTHOR: squareyun

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for case in range(1, T+1):
    N = int(input())
    prices = list(map(int,input().split()))
    answer = 0
    maxPrice = prices[-1]
    for i in range(N-1, -1, -1):
        if prices[i] < maxPrice:
            answer += maxPrice - prices[i]
        else:
            maxPrice = prices[i]
    print('#{} {}'.format(case, answer))