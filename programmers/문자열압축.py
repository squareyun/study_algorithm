# TITLE: 구슬 탈출 (https://school.programmers.co.kr/learn/courses/30/lessons/60057)
# TAG: implementation, bruteforce
# DATE: 20220809
# AUTHOR: squareyun

def solution(s):
    answer = [len(s)]

    for cut in range(1, len(s) // 2 + 1): # 자를 수 있는 범위 (최소 2개 최대 절반개)
        substrIdx = 0
        cutstr = '' # 압축된 문자열을 임시저장
        while substrIdx < len(s):
            substr = s[substrIdx:substrIdx+cut] # 압축의 기준이 되는 문자열
            count = 1 # 압축 횟수
            for checkIdx in range(substrIdx + cut, len(s) - cut + 1, cut):
                checkstr = s[checkIdx:checkIdx+cut] # 동일한 문자열인지 확인하는 문자열
                if substr == checkstr:
                    count += 1
                    substrIdx += cut # 압축했으면 중복으로 확인하면 안됨
                else: break
            if count != 1: # 압축 문자열
                cutstr = cutstr + str(count) + substr
            elif len(substr) == cut: # 압축되지 않는 문자열
                cutstr = cutstr + checkstr
            else: # 압축되지 않는 문자열의 나머지 문자열
                cutstr = cutstr + substr
            substrIdx += cut

        answer.append(len(cutstr))

    return min(answer)

def solution2(s):
    answer = len(s)
    for cut in range(1, len(s) // 2 + 1):
        ts = ""
        idx = 0
        while idx < len(s):
            target = s[idx:idx+cut]
            spli = s[idx:].split(target)
            num = 0
            if spli[-1] == "": spli = spli[:-1]
            for i in spli:
                if i == "":
                    num += 1
                else:
                    break
            if num > 1:
                ts += str(num) + target
            else:
                ts += target
            idx += num * cut
        if idx < len(s):
            ts += s[idx:]
        answer = min(answer, len(ts))
    return answer