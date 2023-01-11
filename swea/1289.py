#TITLE: 원재의 메모리 복구하기
#LEVEL: D3
#DATE: 20230111

T = int(input())
for test_case in range(1, T + 1):
    a = list(map(int, input()))
    history = a[0]
    cnt = 0 if a[0] == 0 else 1
    for i in range(1, len(a)):
        if a[i] != history:
            cnt += 1
            history = a[i]
    print(f'#{test_case} {cnt}')