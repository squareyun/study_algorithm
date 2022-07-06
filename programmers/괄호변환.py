def solution(p):
    if isValid(p): return p
    else: return recur(p)

def recur(w):
    if w == '': return ''
    
    u, v = splitBalance(w)
    if isValid(u):
        return u + recur(v)
    else:
        t = []
        t = '('
        t += recur(v)
        t += ')'
        
        #4-4
        u = u[1:-1]
        l = list(u)
        for i in range(len(l)):
            if l[i] == '(': l[i] = ')'
            elif l[i] == ')': l[i] = '('
        u = ''.join(l)
        
        return t + u

def splitBalance(s):
    left = right = idx = 0
    
    for i in s:
        if i == '(': left += 1
        elif i == ')': right += 1
        if left == right: break
        idx += 1
    
    return s[:idx+1], s[idx+1:]

def isValid(s):
    stack = []

    for i in s:
        stack.append(i)
        if len(stack) >= 2:
            if stack[-1] == ')' and stack[-2] == '(':
                stack.pop()
                stack.pop()
    if len(stack) != 0: return False
    else: return True

print(solution("()(())())"))
# print(isValid("(()())()"))