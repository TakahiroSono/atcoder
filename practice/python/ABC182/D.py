N = int(input())
A = list(map(int, input().split()))
sum_a = [0] * N
max_a = [0] * N

for i in range(N):
  sum_a[i] = sum_a[i-1] + A[i]
  max_a[i] = max(max_a[i-1], sum_a[i])

now = 0
ans = 0

for i in range(N):
  ans = max(ans, now + max_a[i])
  now += sum_a[i]

print(ans)
