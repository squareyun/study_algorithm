# PyPy3로 제출해야 시간초과 나지 않음

def dfs(i):
    visited[i] = True
    for j in graph[i]:
        flag = False
        if b[j] == -1: flag = True
        elif visited[b[j]] == False and dfs(b[j]): flag = True

        if flag:
            a[i] = j
            b[j] = i
            return True
    return False

n, m = map(int, input().split())

graph = []

for i in range(n):
    t = list(map(int, input().split()))
    graph.append(t[1:])

match = 0
a = [-1] * (n + 1)
b = [-1] * (m + 1)

for i in range(n):
    if a[i] == -1:
        visited = [False] * (n + 1)
        if dfs(i):
            match += 1

print(match)