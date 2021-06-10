N, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
S = [[0] * (N + 1)for _ in range(N + 1)]

ng = -1
ok = 10**9
lim = (K*K) // 2 + 1

while ng + 1 < ok:
  x = (ng + ok) // 2;
  for i in range(1, N + 1):
    for j in range(1, N + 1):
      S[i][j] = S[i][j - 1] + S[i - 1][j] - S[i - 1][j - 1]
      if A[i - 1][j - 1] > x: S[i][j] += 1
  ext = False

  for i in range(N - K + 1):
    for j in range(N - K + 1):
      if S[i + K][j + K] + S[i][j] - S[i][j + K] - S[i + K][j] < lim:
        ext = True
  if ext: ok = x
  else: ng = x

print(ok)
