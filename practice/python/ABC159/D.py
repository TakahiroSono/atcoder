N = int(input())
A = list(map(int, input().split()))

ind_A = {}

for i in range(N):
  if A[i] in ind_A:
    ind_A[A[i]] += 1
  else:
    ind_A[A[i]] = 1

ans = 0

for (i, v) in ind_A.items():
  ans += (v * v - v) // 2


for i in range(N):
  value = ind_A[A[i]]
  print(ans - value + 1)
