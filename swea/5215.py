#TITLE: 햄버거 다이어트
#LEVEL: D3
#DATE: 20230111

from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N, L = map(int, input().split())
    ingredient = []
    for _ in range(N):
        ingredient.append(list(map(int, input().split())))
    
    answer = -1
    for cnt in range(1, L):
        for comb in combinations(ingredient, cnt):
            sum = 0
            score = 0
            for i in comb:
                sum += i[1]
                score += i[0]
                if sum > L:
                    break
            if sum <= L:
                answer = max(answer, score)
    print(f'#{test_case} {answer}')