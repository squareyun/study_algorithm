# https://school.programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []
    s_split = s.split("}")
    arr = []
    for i in s_split:
        if i == '': break
        t = i.replace("{", "")
        t = t.split(",")
        if t[0] == '':
            del t[0]
        t = list(map(int, t))
        arr.append(t)

    arr.sort(key=len)
    for i in arr:
        for j in i:
            if j not in answer:
                answer.append(j)
    return answer