#TITLE: 스도쿠 검증
#LEVEL: D2
#DATE: 20230102

T = int(input())

for test_case in range(1, T + 1):
    sudoku = []
    res = True
    for _ in range(9):
        a = list(map(int,input().split()))
        if len(set(a)) != 9:
            res = False
        sudoku.append(a)
    
    if not res:
        print(f'#{test_case} 0')
        continue
    
    sudoku = list(map(list, zip(*sudoku))) # list transpose
    for i in range(9):
        if len(set(sudoku[i])) != 9:
            res = False
            break

    if not res:
        print(f'#{test_case} 0')
        continue

    for i in range(0, 7, 3):
        t = []
        for j in range(0, 7, 3):
            for k in range(3):
                t.extend(sudoku[k+i][j:j+3])
            if len(set(t)) != 9:
                res = False
                break
            t = []
        if not res:
            break
    
    if not res:
        print(f'#{test_case} 0')
    else:
        print(f'#{test_case} 1')