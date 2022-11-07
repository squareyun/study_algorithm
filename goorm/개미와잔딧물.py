n,m=map(int,input().split())
gaemijib=[]
suaek=[]
answer=0
for i in range(n):
	a = list(map(int,input().split()))
	for j in range(n):
		if a[j] == 1:
			gaemijib.append((i,j))
		elif a[j] == 2:
			suaek.append((i,j))

for gx, gy in gaemijib:
	for sx, sy in suaek:
		if abs(gx-sx) + abs(gy-sy) <= m:
			answer += 1
			break
print(answer)