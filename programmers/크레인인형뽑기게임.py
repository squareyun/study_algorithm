def solution(board, moves):
    answer = 0
    stack = []

    # transpose the list
    boardT = [list(x) for x in zip(*board)]

    for i in moves:
        location = i - 1

        # 꺼낼 위치 찾기 (j)
        slot = boardT[location]
        j = len(slot) - 1
        while j > 0:
            if slot[j - 1] == 0:
                break
            else: j -= 1

        if slot[j] != 0:
            stack.append(slot[j])
            slot[j] = 0 # 꺼내기

        # 터트림 확인
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2

    return answer