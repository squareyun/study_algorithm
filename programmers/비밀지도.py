# TITLE: 비밀지도 (https://school.programmers.co.kr/learn/courses/30/lessons/17681)
# LEVEL: 1
# TAG: kakao
# DATE: 20220902
# AUTHOR: squareyun

def make(i,arr, n):
    t=bin(arr[i])[2:]
    t=(n-len(t))*"0"+t
    return t

def solution(n, arr1, arr2):
    answer = []
    map1=[]
    map2=[]
    for i in range(n):
        map1.append(make(i,arr1,n))
        map2.append(make(i,arr2,n))
    for i in range(n):
        t=""
        for j in range(n):
            if int(map1[i][j]) + int(map2[i][j]) == 0:
                t+=" "
            else:
                t+="#"
        answer.append(t)
    return answer