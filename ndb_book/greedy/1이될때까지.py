# 내 풀이
# n이 100억 이상의 큰 수가 되었을 때 시간초과 우려

# import time
# start = time.time()
# n, k = map(int, input().split())

# count = 0

# while True:
#     if n == 1:
#         break

#     if n % k == 0:
#         n /= k
#     else:
#         n -= 1

#     count += 1

# print(count)
# print("execute time: ", time.time() - start)


# 책 풀이
import time
start = time.time()

n, k = map(int, input().split())
result = 0
while True:
    # N == K로 나누어떨어지는 수가 될 때까지 1씩 빼기
    target = (n // k) * k
    result += (n - target)
    n = target
    
    if n < k:
        break

    # K로 나누기
    n //= k
    result += 1

result += (n - 1)
print(result)
print("execute time: ", time.time() - start)