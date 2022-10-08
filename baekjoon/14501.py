#TITLE: 퇴사 (https://www.acmicpc.net/problem/14501)
#LEVEL: S3
#TAG: brute-force, recursion
#DATE: 20221008
#AUTHOR: squareyun

n=int(input())
tp=[]
for _ in range(n):
    tp.append(list(map(int,input().split())))

def solution(day, remain, money):
    if day == n:
        if remain > 0:
            return 0
        else:
            return money
    
    result = solution(day+1, remain-1, money) #해당 날짜 상담 X
    if remain <= 0: #상담 진행 아닐 때
        result = max(result, solution(day+1, tp[day][0]-1, money+tp[day][1])) #해당 날짜 상담 O
    return result

print(solution(0,0,0))