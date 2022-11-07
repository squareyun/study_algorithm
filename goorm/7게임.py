def solution(s):
	a = 0
	for i in range(len(s)):
		if i % 2 == 0:
			a += int(s[i])
	
	for i in range(len(s)):
		if i % 2 == 1:
			if s[i] != '0':
				a *= int(s[i])
		
	return a % 10

for _ in range(5):
	s = input()
	print(solution(s))