n = int(input())
s = input()
answer = ""
for i in range(0, n, 2):
	t = ord(s[i]) + int(s[i+1]) ** 2
	if t > ord('z'):
		t = ord('a') + (t - ord('a')) % 26
	answer += chr(t)
print(answer)   