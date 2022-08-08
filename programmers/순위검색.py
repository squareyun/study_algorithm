# TITLE: 순위 검색 (https://school.programmers.co.kr/learn/courses/30/lessons/72412)
# LEVEL: 2
# TAG: kakao
# DATE: 20220808
# AUTHOR: squareyun

def searchindex(score, target):
    l = 0; r = len(score)
    while True:
        m = (l+r)//2
        mNum = score[m][1]
        if mNum == target:
            while score[m][1] == target:
                m-=1
            return m+1
        elif abs(l-r)<=1:
            return m+1

        if mNum > target:
            r = m - 1
        else:
            l = m          

def solution(info, query):
    answer = []; data=[]; score=[]
    for i in range(len(info)):
        t=info[i].split()
        data.append(t[:-1])
        score.append((i, int(t[-1])))
    
    score.sort(key=lambda x:x[1])
    
    for i in range(len(query)):
        target=query[i].split(" and ")
        t = target[-1].split(" ")
        target[-1] = t[0]
        tscore = int(t[1])
        
        sidx = searchindex(score, tscore)
        searchidx=set()
        for j in range(sidx,len(score)):
            searchidx.add(score[j][0])
        
        tsearchidx=searchidx.copy()
        for j in range(4):
            if target[j] == '-': continue
            for k in searchidx:
                if k not in tsearchidx: continue
                if data[k][j] != target[j]:
                    tsearchidx.remove(k)
        answer.append(len(tsearchidx))
        
    return answer

info=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
query=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
print(solution(info,query))