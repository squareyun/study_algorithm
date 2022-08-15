# TITLE: 광고 삽입 (https://school.programmers.co.kr/learn/courses/30/lessons/72414)
# TAG: kakao, dp
# DATE: 20220815
# AUTHOR: squareyun
# REFERENCE: https://dev-note-97.tistory.com/156

def solution(play_time, adv_time, logs):
    t = play_time.split(":")
    play_time = int(t[0]) * 60 * 60 + int(t[1]) * 60 + int(t[2])
    t = adv_time.split(":")
    adv_time = int(t[0]) * 60 * 60 + int(t[1]) * 60 + int(t[2])
    
    times = [0 for _ in range(play_time + 1)]

    for l in logs:
        k = l.split("-")
        t1 = k[0].split(":")
        t2 = k[1].split(":")
        start = int(t1[0]) * 60 * 60 + int(t1[1]) * 60 + int(t1[2])
        end = int(t2[0]) * 60 * 60 + int(t2[1]) * 60 + int(t2[2])
        times[start] += 1
        times[end] -= 1
    
    for i in range(1, len(times)):
        times[i] = times[i-1] + times[i]

    for i in range(1, len(times)):
        times[i] = times[i-1] + times[i]

    most_view = 0
    answer = 0
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < times[i] - times[i-adv_time]:
                most_view = times[i] - times[i-adv_time]
                answer = i - adv_time + 1
        else:
            if most_view < times[i]:
                most_view = times[i]
                answer = i - adv_time + 1
    
    h = answer // 3600
    h = '0' + str(h) if h < 10 else str(h)
    answer = answer % 3600
    m = answer // 60
    m = '0' + str(m) if m < 10 else str(m)
    answer = answer % 60
    s = '0' + str(answer) if answer < 10 else str(answer)
    return h + ':' + m + ':' + s