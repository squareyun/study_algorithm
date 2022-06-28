def solution(numbers):
    answer = 0
    
    target = [1 for _ in range(10)]
    
    for i in numbers:
        target[i] = 0
    
    for i in range(len(target)):
        if target[i] == 1:
            answer += i
    
    return answer