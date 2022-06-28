answer = 0

def solution(numbers, target):
    dfs(numbers, target, 0)
    return answer

def dfs(numbers, target, now):
    global answer

    if len(numbers) == 1:
        if now + numbers[0] == target or now - numbers[0] == target:
            answer += 1
        return
    
    
    dfs(numbers[1:], target, now + numbers[0])
    dfs(numbers[1:], target, now - numbers[0])
    