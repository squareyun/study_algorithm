def solution(id_list, report, k):
    answer = []
    
    report = list(set(report)) # set을 이용해 중복으로 신고한 내역 제거
    
    d_accumulate = dict.fromkeys(id_list, 0) # 누적 신고 횟수를 담는 dictionary
    email = set() # 불량 이용자 이름
    for r in report:
        s = r.split()
        d_accumulate[s[1]] += 1
        if d_accumulate[s[1]] >= k: # 누적 신고 횟수가 k번 넘으면 불량 이용자로 등록
            email.add(s[1])
    
    send = dict.fromkeys(id_list, 0) # 이메일 보낼 횟수를 담는 dictionary
    for r in report:
        s = r.split()
        if s[1] in email:
            send[s[0]] += 1
    
    # return 배열 구성
    for key, value in send.items():
        answer.append(value)
    
    return answer