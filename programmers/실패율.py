def solution(N, stages):
    answer = [0] * (N+1)
    
    stages.sort()
    
    i = 0
    while i != len(stages):
        cur = stages[i]
        
        challenger = 1
        temp_i = i + 1
        while temp_i != len(stages) and cur == stages[temp_i]:
            challenger += 1
            temp_i += 1
            if temp_i == len(stages): break
        
        index = cur
        if cur < N:
            answer[index] = challenger / (len(stages) - i)
        elif cur == N:
            allClear = 0
            while temp_i != len(stages) and N + 1 == stages[temp_i]:
                temp_i += 1
                allClear += 1
            answer[index] = challenger / (challenger + allClear)
            
        else: break
        
        i = temp_i
    
    sortArr = []
    for i in range(1, N+1):
        sortArr.append((answer[i], i))
    
    sortArr = sorted(sortArr, key=lambda x: (-x[0], x[1]))
    answer = []
    for i in range(N):
        answer.append(sortArr[i][1])
    
    return answer