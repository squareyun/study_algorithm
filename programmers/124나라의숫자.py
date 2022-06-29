def solution(n):
    answer = ''
        
    while n > 0:
        n, mod = n // 3, n % 3
        if mod == 0:
            n -= 1
            answer += '4'
        elif mod == 1:
            answer += '1'
        elif mod == 2:
            answer += '2'
    
    return answer[::-1]