n = int(input())
A = list(map(int, input().split()))

mod = [0] * 210

ans = 0
for a in A:
  mod[a % 200] += 1

for m in mod:
  if m < 2: continue
  ans += (m * (m - 1)) / 2

print(int(ans))
