N = int(input())
a = list(map(int, input().split()))
answer = []
	
def isError(k):
	while k > 1:
		if k % 2 != 0:
			return True
		k /= 2
	if k == 1:
		return False

for i in range(len(a)):
	if isError(a[i]):
		answer.append(i+1)
		
print(len(answer))
print(*answer)