K, N = map(int, input().split())
A = list(map(int, input().split()))

sumA = A[-1] - A[0]
Ai = sumA

for i in range(1, N):
  sumA = min(sumA, (A[i-1] + K) - A[i])

print(sumA)
