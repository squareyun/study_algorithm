#TITLE: 마인크래프트 (https://www.acmicpc.net/problem/18111)
#LEVEL: S2
#TAG: brute-force, implementation
#DATE: 20221008
#AUTHOR: squareyun

n,m,b=map(int,input().split())
INF=int(1e9)
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

lower=min([min(x) for x in board])
upper=max([max(x) for x in board])

def solution(target, remain):
    time = 0
    use=0

    for i in range(n):
        for j in range(m):
            cost = board[i][j] - target
            if cost > 0:
                remain += cost
                time += 2*cost
            else:
                use += -cost

    if remain < use:
        return INF

    return time + use

answer=[INF,INF]
for i in range(upper, lower-1, -1):
    ret = solution(i, b)
    if ret < answer[0]:
        answer = [ret, i]
print(answer[0], answer[1])