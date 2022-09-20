# TITLE: 성격 유형 검사하기 (https://school.programmers.co.kr/learn/courses/30/lessons/118666)
# LEVEL: 1
# TAG: kakao
# DATE: 20220920
# AUTHOR: squareyun

def solution(survey, choices):
    answer = ''
    d={'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    for i in range(len(survey)):
        if choices[i] > 4:
            d[survey[i][1]] += choices[i] - 4
        elif choices[i] < 4:
            d[survey[i][0]] += 4 - choices[i]
    
    answer += 'R' if d['R'] >= d['T'] else 'T'
    answer += 'C' if d['C'] >= d['F'] else 'F'
    answer += 'J' if d['J'] >= d['M'] else 'M'
    answer += 'A' if d['A'] >= d['N'] else 'N'
    return answer