#TITLE: 1204. [S/W 문제해결 기본] 1일차 - 최빈수 구하기
#LEVEL: D2
#DATE: 20230105

T = int(input())

for test_case in range(1, T + 1):
    input()
    cnt = [0 for _ in range(101)]
    arr = list(map(int,input().split()))
    for i in range(1000):
        cnt[arr[i]] += 1

    maxCnt = -1
    maxIndex = -1
    for i in range(101):
        if maxCnt <= cnt[i]:
            maxCnt = cnt[i]
            maxIndex = i
    print(f'#{test_case} {maxIndex}')