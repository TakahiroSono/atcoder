N = int(input())
A = list(map(int, input().split()))
sum_a = [0] * N
sub_a = [0] * N

sum_a[0] = A[0]
sub_a[-1] = A[-1]
for i in range(1, N):
  sum_a[i] += sum_a[i-1] + A[i]
  sub_a[N-i-1] += sub_a[N-i] + A[N-i-1]

ind = -1
for i in range(N-1, -1, -1):
  if sum_a[i] >= 0:
    ind = i + 1
    break

ans = 0
for i in range(ind):
  ans += sum_a[i] * (ind - i)

print(ans)
