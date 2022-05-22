def solution(new_id):
    answer = ''
    
    # 1단계
    answer = new_id.lower()
    
    # 2단계
    delete = "~!@#$%^&*()=+[{]}:?,<>/"
    for i in range(len(delete)):
        answer = answer.replace(delete[i], "")

    # 3단계
    while answer.replace("..", "") != answer:
        answer = answer.replace("..", ".")
        
    # 4단계
    if len(answer) > 0:
        if answer[0] == '.': answer = answer[1:]
    if len(answer) > 0:
        if answer[-1] == '.': answer = answer[:-1]
    
    # 5단계
    if len(answer) == 0:
        answer = "a"
    
    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    
    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer = answer + answer[-1]

    return answer
