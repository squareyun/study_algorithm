#TITLE: [S/W 문제해결 기본] 2일차 - Sum
#LEVEL: D2
#DATE: 20230105

for test_case in range(1, 11):
    input()
    arr = []

    rowSum = [0 for _ in range(100)]
    columnSum = [0 for _ in range(100)]
    diagonal1 = 0
    diagonal2 = 0

    for i in range(100):
        arr.append(list(map(int,input().split())))
        rowSum[i] = sum(arr[i])
        
        for j in range(100):
            columnSum[j] += arr[i][j]
            if i == j:
                diagonal1 += arr[i][j]
            if j == (100-i):
                diagonal2 += arr[i][j]
    
    answer = max(max(rowSum), max(columnSum), diagonal1, diagonal2)

    print(f'#{test_case} {answer}')