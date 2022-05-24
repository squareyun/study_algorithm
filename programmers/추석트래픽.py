def solution(lines):
    answer = 0
    log = []

    for s in lines:
        date, time, long = s.split()
        hh, mm, ss = time.split(":")
        t = long.replace("s", "")

        end = (int(hh) * 60 * 60 + int(mm) * 60 + float(ss)) * 1000
        start = end - float(t) * 1000 + 1
        log.append([start, end])

    for i in log:
        answer = max(answer, calculate(log, i[0], i[0] + 1000), calculate(log, i[1], i[1] + 1000))

    return answer

def calculate(log, start, end):
    cnt = 0
    for i in log:
        if i[0] < end and i[1] >= start:
            cnt += 1
    return cnt
