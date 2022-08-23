# TITLE: 후보키 (https://school.programmers.co.kr/learn/courses/30/lessons/42890)
# TAG: kakao, implementation, set, combination
# DATE: 20220823
# AUTHOR: squareyun

from itertools import combinations

def solution(relation):
    col = len(relation[0])
    candidates = []
    for i in range(1, col + 1):
        for combi in combinations(range(col), i):
            temp = []
            for r in relation:
                curr = [r[c] for c in combi]
                if curr in temp:
                    break
                else:
                    temp.append(curr)
            else:
                for ck in candidates:
                    if set(ck).issubset(set(combi)):
                        break
                else:
                    candidates.append(combi)
    return len(candidates)