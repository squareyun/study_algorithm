# TITLE: 모의고사 (https://school.programmers.co.kr/learn/courses/30/lessons/42840)
# LEVEL: 1
# TYPE: bruteforce
# DATE: 20220806
# AUTHOR: squareyun

def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    temp = [0,0,0]
    for i in range(len(answers)):
        k = answers[i]
        if a[i%5] == k:
            temp[0] += 1
        if b[i%8] == k:
            temp[1] += 1
        if c[i%10] == k:
            temp[2] += 1
            
    maxvalue = max(temp)
    
    for i in range(3):
        if temp[i] == maxvalue:
            answer.append(i + 1)
    
    return answer