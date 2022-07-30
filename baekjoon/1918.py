# 후위 표기식 (https://www.acmicpc.net/problem/1918)
str=input()
ops={"*":2, "/":2, "+":1, "-":1, "(":0}
stack=[]
answer=""
for s in str:
    if s.isalpha():
        answer+=s
    elif s == "(":
        stack.append(s)
    elif s == ")":
        while stack:
            t=stack.pop()
            if t != "(": answer+=t
            else: break
    else:
        while stack and ops[stack[-1]] >= ops[s]:
            answer+=stack.pop()
        stack.append(s)
while stack:
    answer+=stack.pop()
print(answer)