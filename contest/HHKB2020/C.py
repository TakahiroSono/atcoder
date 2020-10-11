N = int(input())
P = list(map(int, input().split()))

set_p = set()
ans = 0
for i in range(N):
  set_p.add(P[i])
  if P[i] == ans:
    ans += 1
    while ans in set_p:
      ans += 1
  print(ans)
