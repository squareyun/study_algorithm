def solution(record):
    answer = []
    
    nickname = dict();
    for string in record:
        s = string.split()
        if s[0] == 'Enter' or s[0] == 'Change':
            nickname[s[1]] = s[2]
    
    for string in record:
        s = string.split()
        
        if s[0] == 'Enter':
            out1 = "들어왔습니다."
        elif s[0] == 'Leave':
            out1 = "나갔습니다."
        else:
            continue
        
        out2 = nickname[s[1]] + "님이 " + out1
        answer.append(out2)
    
    return answer