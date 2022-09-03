# TITLE: 프렌즈4블록 (https://school.programmers.co.kr/learn/courses/30/lessons/17679)
# LEVEL: 2
# TAG: kakao
# DATE: 20220904
# AUTHOR: squareyun

import string
def solution(m, n, board):
    answer = 0
    finish = False
    while not finish:
        total = dict((key, set()) for key in string.ascii_uppercase) #https://bit.ly/3QdCrRA
        for i in range(m-1):
            kernel = [[i,0],[i,1],[i+1,0],[i+1,1]]
            for j in range(n-1):
                for k in range(2):
                    kernel[k][1] = j + k
                    kernel[k+2][1] = j + k
                #커널 초기화 완료
                block=board[kernel[0][0]][kernel[0][1]]
                if block == ' ':
                    continue
                flag=True
                for k in range(1,4):
                    if block != board[kernel[k][0]][kernel[k][1]]:
                        flag=False
                        break
                if flag:
                    for a in kernel:
                        total[block].add(tuple(a))
        finish = True
        for _, value in total.items():
            if len(value) > 0:
                answer += len(value)
                for v in value:
                    t = board[v[0]]
                    board[v[0]] = t[0:v[1]] + ' ' + t[v[1]+1:n]
                finish = False
        if not finish:
            #타일 내리기
            for k in range(m):
                for i in range(1,m):
                    for j in range(n):
                        if board[i][j] == ' ' and board[i-1][j] != ' ':
                            board[i] = board[i][0:j] + board[i-1][j] + board[i][j+1:n]
                            board[i-1] = board[i-1][0:j] + ' ' + board[i-1][j+1:n]

    return answer