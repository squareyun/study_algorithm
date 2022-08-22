# TITLE: 궁금한 민호 (https://www.acmicpc.net/problem/1507)
# LEVEL: Gold 2
# TAG: floyd_warshall, graph
# DATE: 20220822
# AUTHOR: squareyun

n=int(input())
flag=[[[True] for _ in range(n)] for _ in range(n)]
graph=[]

for i in range(n):
    graph.append(list(map(int,input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if i==j or j==k or k==i: continue
            if graph[i][j] == graph[i][k] + graph[k][j]:
                flag[i][j] = False
            elif graph[i][j] > graph[i][k] + graph[k][j]:
                print(-1)
                exit(0)

answer=0
for i in range(n):
    for j in range(i, n):
        if flag[i][j]:
            answer += graph[i][j]
print(answer)