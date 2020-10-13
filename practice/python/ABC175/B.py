N = int(input())
L = list(map(int, input().split()))

cnt = 0

for i in range(N):
  for j in range(i+1, N):
    for k in range(j+1, N):
      big, small = max(L[i], L[j]), min(L[i], L[j])
      cnt += big - small < L[k] < big + small and L[i] != L[j] != L[k] != L[i]

print(cnt)
