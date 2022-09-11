#TITLE: 파괴되지 않은 건물 (https://school.programmers.co.kr/learn/courses/30/lessons/92344)
#LEVEL: 3
#TAG: kakao, dp
#DATE: 20220911
#REFERENCE: https://bit.ly/3B90LOJ

def solution(board, skills):
    update = [[0] * (len(board[0])+1) for _ in range(len(board)+1)]
    for skill, r1, c1, r2, c2, degree in skills:
        if skill == 1:
            degree *= (-1)
            
        update[r1][c1] += degree
        update[r2+1][c2+1] += degree
        update[r1][c2+1] += degree * (-1)
        update[r2+1][c1] += degree * (-1)
    
    # 누적합
    for i in range(1, len(update)):
        for j in range(0, len(update[0])):
            update[i][j] += update[i-1][j]
    
    for i in range(1, len(update[0])):
        for j in range(0, len(update)):
            update[j][i] += update[j][i-1]
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += update[i][j]
        
    answer=len(board)*len(board[0])
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] <= 0:
                answer -= 1
    return answer