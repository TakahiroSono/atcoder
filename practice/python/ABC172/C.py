N, M, K = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

for i in range(1, N+1):
  A[i] += A[i-1]

for i in range(1, M+1):
  B[i] += B[i-1]


ans = 0
b_count = M
for a_count in range(N+1):
  if A[a_count] > K:
    continue

  while A[a_count] + B[b_count] > K:
    b_count -= 1

  ans = max(ans, a_count + b_count)
print(ans)
