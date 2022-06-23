def solution(s):
    answer = ''
    word = {'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9}

    i = 0
    while i < len(s):
        target = s[i]
        if target.isdecimal():
            answer += target
            i += 1
            continue
        
        temp = ''
        while not target.isdecimal():
            temp += target
            try:
                answer += str(word[temp])
                i += 1
                break
            except:
                i += 1
                if i >= len(s): break
                target = s[i]
        
    return int(answer)