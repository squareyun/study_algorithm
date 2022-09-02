# TITLE: 다트게임 (https://school.programmers.co.kr/learn/courses/30/lessons/17682)
# LEVEL: 1
# TAG: kakao
# DATE: 20220902
# AUTHOR: squareyun

def solution(dartResult):
    num=0
    score=[0,0,0]
    scoreIdx=0
    for a in range(len(dartResult)):
        i=dartResult[a]
        if a > 0 and dartResult[a-1:a+1]=='10':
            i='10'
        if i=='*':
            if scoreIdx == 1:
                score[scoreIdx-1]*=2
            else:
                score[scoreIdx-2]*=2
                score[scoreIdx-1]*=2
        elif i=='#':
                score[scoreIdx-1]*=(-1)
        elif i.isdecimal():
            num=int(i)
            continue
        elif i=='S':
            score[scoreIdx]=num
            scoreIdx+=1
        elif i=='D':
            score[scoreIdx]=num**2
            scoreIdx+=1
        elif i=='T':
            score[scoreIdx]=num**3
            scoreIdx+=1
            
    return sum(score)