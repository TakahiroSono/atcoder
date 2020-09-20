N = int(input())
A = list(map(int, input().split()))
max = A[0]
ans = 0

for a in A[1:]:
  if a < max:
    ans += max - a
  else:
    max = a

print(ans)
