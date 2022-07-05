from itertools import combinations

def solution(orders, course):
    answer = []
    
    maxLen = len(max(orders, key=len))
    
    for c in course:
        if c > maxLen: continue
        
        # order를 탐색하면서
        checkTwoList = []
        checkTwoMax = 0
        
        for order in orders:
            if len(order) < c: continue
            
            # 순열 구해서 orders를 순회하며 해당 순열이 모두 포함되면 answer에 넣기
            splits = list(order)
            for comb in combinations(splits, c):
                checkTwo = 0

                for order in orders:
                    checkC = 0
                    for i in comb:
                        checkC += order.count(i)
                    if checkC >= c: checkTwo += 1

                if checkTwo >= 2:
                    if checkTwo > checkTwoMax: checkTwoMax = checkTwo
                    checkTwoList.append((checkTwo, ''.join(comb)))
            
        for i in checkTwoList:
            if i[0] == checkTwoMax:
                answer.append(i[1])
                
    for i in range(len(answer)):
        answer[i] = ''.join(sorted(answer[i]))
        
    answer = list(set(answer))    
    answer.sort()
    
    return answer