from itertools import product

N, K = map(int, input().split())
T = [[0]* N for _ in range(N)]

for n in range(N):
  T[n] = list(map(int, input().split()))

ans = 0
for itr in product(range(N - 1), repeat=(N-1)):
  set_itr = set(itr)
  cnt = 0
  now = 0
  if len(set_itr) == N-1:
    for i in itr:
      cnt += T[now][i+1]
      now = i + 1
    cnt += T[now][0]
    if cnt == K:
      ans += 1
  else:
    continue

print(ans)
