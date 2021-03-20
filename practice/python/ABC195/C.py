N = int(input())

n = 1000
cnt = 0

while n < N:
  cnt += N % n
  cnt += N - n + 1
  n *= 1000

print(cnt)
