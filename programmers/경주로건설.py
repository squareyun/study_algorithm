# TITLE: 경주로 건설 (https://school.programmers.co.kr/learn/courses/30/lessons/67259)
# LEVEL: 3
# TAG: kakao
# DATE: 20220922
# REFERENCE: https://bit.ly/3C1qxpU

from collections import deque

def solution(board):
    n = len(board)
    cost = [[[float('inf')] * n for _ in range(n)] for _ in range(4)]
    dx = [-1,1,0,0] #UDRL
    dy = [0,0,1,-1]
    q = deque()
    
    for i in range(4):
        cost[i][0][0] = 0
    
    if board[0][1] == 0:
        q.append((0, 1, 2, 100)) #(x, y, direction, cost)
        cost[2][0][1] = 100 #2: 동쪽
    
    if board[1][0] == 0:
        q.append((1, 0, 1, 100))
        cost[1][1][0] = 100 #1: 남쪽
    
    while q:
        x, y, d, c = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                new_cost = c + 100 if d == i else c + 600
                if cost[i][nx][ny] > new_cost:
                    cost[i][nx][ny] = new_cost
                    q.append((nx, ny, i, new_cost))
    
    answer = float('inf')
    for i in range(4):
        answer = min(answer, cost[i][-1][-1])
    return answer
