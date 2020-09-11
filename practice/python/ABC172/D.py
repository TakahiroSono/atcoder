def calc(b, e):
  cnt = e // b
  return (b + e) * cnt // 2

N = int(input())

ans = 0

for i in range(1, N+1):
  ans += calc(i, N//i * i)

print(ans)
