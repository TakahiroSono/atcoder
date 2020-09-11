N = int(input())
A = list(map(int, input().split()))

ans = 0
for a in A[::2]:
  ans += a % 2
print(ans)
