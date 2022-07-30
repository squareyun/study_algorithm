# 토달기 (https://www.acmicpc.net/problem/1897)
d,word=input().split()
dic=[input() for _ in range(int(d))]
sorted_dic = sorted(dic,key=len)

answer = word
possible = {word : 1}
for s in sorted_dic:
    if s == word: continue
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t in possible:
            possible[s] = 1
            if len(s) > len(answer):
                answer = s
print(answer)