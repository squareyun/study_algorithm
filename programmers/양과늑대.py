#TITLE: 양과 늑대 (https://school.programmers.co.kr/learn/courses/30/lessons/92343)
#LEVEL: 3
#TAG: kakao, backtracking
#DATE: 20220909
#REFERENCE: https://bit.ly/3RP3RhD

def solution(info, edges):
    visited = [0] * len(info)
    visited[0] = 1
    answer = []

    def dfs(sheep, wolf):
        if sheep > wolf:
            answer.append(sheep)
        else:
            return

        for i in range(len(edges)):
            parent, child = edges[i]
            isWolf = info[child]
            if visited[parent] and not visited[child]:
                visited[child] = 1
                dfs(sheep + (isWolf == 0), wolf + (isWolf == 1))
                visited[child] = 0
    dfs(1, 0)
    return max(answer)