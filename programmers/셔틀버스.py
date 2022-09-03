# TITLE: 셔틀버스 (https://school.programmers.co.kr/learn/courses/30/lessons/17678)
# LEVEL: 3
# TAG: kakao
# DATE: 20220903
# AUTHOR: squareyun

def solution(n, t, m, timetable):
    answer = -1
    time=[]
    for i in timetable:
        hh, mm = i.split(":")
        time.append(int(hh)*60 + int(mm))
    time.sort()
    
    busStops=[540 + t * i for i in range(n)]
    
    i=0
    for busStop in busStops:
        cnt=0
        while cnt<m and i < len(time) and time[i] <= busStop:
            cnt += 1
            i += 1
        if cnt < m: # 버스에 자리가 남으면
            answer = busStop
        else: # 버스에 자리가 남지 않을 때 마지막 탄 사람보다 앞에
            answer = time[i-1] - 1
    
    hh,mm=divmod(answer,60)
    if hh < 10:
        answer='0'+str(hh)+':'
    else:
        answer=str(hh)+':'
    if mm < 10:
        answer+='0'+str(mm)
    else:
        answer+=str(mm)
    return answer

print(solution(10,25,1, ["09:00", "09:10", "09:20", "09:30", "09:40", "09:50", "10:00", "10:10", "10:20", "10:30", "10:40", "10:50"]))