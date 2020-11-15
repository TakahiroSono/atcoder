N, W = map(int, input().split())
times = [0] * 220000

for _ in range(N):
  s, t, p = map(int, input().split())
  times[s] += p
  times[t] -= p

cnt = 0
for i in range(220000):
  cnt += times[i]
  if cnt > W:
    print('No')
    break
else:
  print('Yes')
