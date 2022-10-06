#TITLE: JadenCase 문자열 만들기 (https://school.programmers.co.kr/learn/courses/30/lessons/12951)
#LEVEL: 2
#TAG: string
#DATE: 20221006
#AUTHOR: squareyun

def solution(s):
    answer = []
    ss = s.split(" ")
    for s in ss:
        if s == '':
            answer.append("")
            continue
        if not s[0].isalpha():
            answer.append(s.lower())
        else:
            t = s[0].upper() + s[1:].lower()
            answer.append(t)
    return ' '.join(answer)