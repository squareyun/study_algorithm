def solution(lottos, win_nums):
    answer = []
    
    zeroCount = lottos.count(0)
    winCount = 0
    for num in lottos:
        if win_nums.count(num) == 1:
            winCount += 1
    best = winCount + zeroCount
    answer.append(7 - best if best > 0 else 6)
    answer.append(7 - winCount if winCount > 1 else 6)
    return answer
