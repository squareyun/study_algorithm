from numpy import array2string


n, m = map(int, input().split())

x, y, dir = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

# d: 방문한 위치 저장
d = [[0] * m for _ in range(n)]
d[x][y] = 1 # 시작 지점

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 1
turnCount = 0
while True:
    # 왼쪽회전
    dir -= 1
    if dir == -1: dir = 3

    nx = x + dx[dir]
    ny = y + dy[dir]
    if d[nx][ny] == 0 and maps[nx][ny] == 0:
        d[nx][ny] = 1
        result += 1
        x = nx
        y = ny
        turnCount = 0
        continue
    else:
        turnCount += 1
    
    if turnCount == 4:
        nx = x - dx[dir]
        ny = y - dy[dir]

        if maps[nx][ny] == 0:
            x = nx
            y = ny
        else:
            break # 종료 조건
        turnCount = 0

print(result)
