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