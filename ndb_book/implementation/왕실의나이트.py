point = input()
row = int(point[1])
col = ord(point[0]) - ord('a') + 1

steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (1, 2), (2, 1), (-2, 1), (-1, 2)]

count = 0
for step in steps:
    nextRow = row + step[0]
    nextCol = col + step[1]

    if 1 <= nextRow <= 8 and 1 <= nextCol <= 8:
        count += 1

print(count)