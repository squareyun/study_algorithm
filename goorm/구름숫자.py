N = int(input())
s = input()
a = [s[0]]
for i in range(1, len(s)-1):
	a.append(s[i])
	a.append(s[i])
a.append(s[-1])
a = "".join(a)

d = {"qw":"1","as":"2","zx":"3","we":"4","sd":"5","xc":"6","er":"7","df":"8","cv":"9","ze":"0"}
answer = []
for i in range(0, len(a), 2):
	if a[i:i+2] in d:
		answer.append(d[a[i:i+2]])
print("".join(answer))