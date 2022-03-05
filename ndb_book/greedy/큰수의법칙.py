n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort(reverse=True)

result = 0
count = 0

for i in range(m):
  if count == k:
    result += data[1]
    count = 0
  else:
    result += data[0]

  count += 1

print(result)