import sys
input=sys.stdin.readline

n,k=map(int,input().split())
a = []
for i in range(n):
	a.append(input().rstrip())

a.sort()
a.sort(key=lambda x: len(x))
print(a[k-1])