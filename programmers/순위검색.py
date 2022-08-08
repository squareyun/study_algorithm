# TITLE: 순위 검색 (https://school.programmers.co.kr/learn/courses/30/lessons/72412)
# LEVEL: 2
# TAG: kakao
# DATE: 20220808
# AUTHOR: squareyun

def searchindex(score, target):
    l = 0; r = len(score)-1
    tmp = len(score)
    while l <= r:
        m = (l+r)//2
        if target <= score[m]:
            tmp = m
            r=m-1
        else:
            l=m+1
    return tmp

def solution(info, query):
    answer=[]
    hash={}
    for i in ['cpp','java','python','-']:
        for j in ['backend','frontend','-']:
            for k in ['junior','senior','-']:
                for l in ['chicken','pizza','-']:
                    hash[i+j+k+l] =  []
    
    for infom in info:
        infom = infom.split(" ")
        for i in [infom[0], '-']:
            for j in [infom[1], '-']:
                for k in [infom[2], '-']:
                    for l in [infom[3], '-']:
                        hash[i+j+k+l].append(int(infom[4]))
    
    for key in hash.keys():
        hash[key].sort()
    
    for sql in query:
        sql = sql.replace(" and ", "")
        sql = sql.split()
        target = int(sql[1])
        sql = sql[0]
        ret = searchindex(hash[sql], target)
        answer.append(len(hash[sql]) - ret)

    return answer