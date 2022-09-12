#TITLE: 단축키 지정 (https://www.acmicpc.net/problem/1283)
#LEVEL: Silver 2
#TAG: implementation, string
#DATE: 20220912
#AUTHOR: squareyun

n=int(input())
menu={}
answer=[]
for _ in range(n):
    inputStr=input()
    s=inputStr.split(" ")
    flag = False
    noFlag = True
    for i in range(len(s)):
        if s[i][0].upper() not in menu:
            menu[s[i][0].upper()] = 1
            s[i] = "[" + s[i][0] + "]" + s[i][1:]
            noFlag = False
            break
        elif i == len(s) - 1:
            flag = True
    if not flag:
        answer.append(' '.join(s))
    else:
        for i in range(len(inputStr)):
            if inputStr[i] == ' ': continue
            if inputStr[i].upper() not in menu:
                menu[inputStr[i].upper()] = 1
                answer.append(inputStr[:i] + "[" + inputStr[i] + "]" + inputStr[i+1:])
                noFlag = False
                break
    if noFlag:
        answer.append(inputStr)
for i in range(n):
    print(answer[i])
