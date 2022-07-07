def solution(str1, str2):
    answer = 0
    
    set1 = makeSet(str1)
    set2 = makeSet(str2)

    # 다중집합의 합집합 구하기
    temp = set1.copy()
    unionSet = set1.copy()
    for i in set2:
        if i not in temp:
            unionSet.append(i)
        else:
            temp.remove(i)
    
    # 다중집합의 교집합 구하기
    temp = set1.copy()
    intersecSet = []
    for i in set2:
        if i in temp:
            temp.remove(i)
            intersecSet.append(i)

    if len(set1) == 0 and len(set2) == 0: return 65536 
    
    answer = int(len(intersecSet) / len(unionSet) * 65536)
    return answer

def makeSet(str):
    setList = []
    str = str.upper()

    i = 0
    while i + 1 < len(str):
        comb = str[i] + str[i+1]
        if comb.isalpha():
            setList.append(comb)
        i += 1
    return setList