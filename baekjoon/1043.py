# TITLE: 거짓말 (https://www.acmicpc.net/problem/1043)
# LEVEL: Gold 4
# TAG: data_structures, disjoint_set, graphs, bruteforce
# DATE: 20220824
# AUTHOR: squareyun

n,m=map(int,input().split())
truth = set(map(int,input().split()[1:]))
parties=[]
for i in range(m):
    parties.append(set((map(int,input().split()[1:]))))
for _ in range(m):
    for party in parties:
        if party & truth: # 교집합 존재 여부 확인
            truth = truth.union(party) # 진실 아는 사람 업데이트 (합집합)
answer=0
for party in parties:
    if not (party & truth):
        answer+=1
print(answer)