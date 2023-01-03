#TITLE: 숫자 배열 회전
#LEVEL: D2
#DATE: 20230103

T = int(input())

'''
before
(0,0) (0,1) (0,2)
(1,0) (1,1) (1,2)
(2,0) (2,1) (2,2)

after
(2,0) (1,0) (0,0)
(2,1) (1,1) (0,1)
(2,2) (1,2) (0,2)
'''
def rotate90(arr, l):
    rotatedArr = [[0] * l for _ in range(l)]
    for i in range(l):
        for j in range(l):
            rotatedArr[i][j] = arr[l-j-1][i]
    return rotatedArr

for test_case in range(1, T + 1):
    arr = []
    l = int(input())
    for _ in range(l):
        arr.append(list(map(int,input().split())))

    answer = [[] for _ in range(l)]

    for i in range(3): # 90도, 180도, 270도
        arr = rotate90(arr, l)
        for j in range(l):
            answer[j].append(''.join(map(str,arr[j]))) # [1, 2, 3]을 ['123']으로 변환 (int로 변환 시 012 표현 불가능)

    print(f'#{test_case}')
    for i in range(l):
        print(*answer[i])