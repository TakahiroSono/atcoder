N, W = map(int, input().split())
dp = [[float('inf')] * 110000 for _ in range(N+1)]

dp[0][0] = 0
for i in range(1, N+1):
  w, v = map(int, input().split())
  for j in range(110000):
    dp[i][j] = dp[i-1][j]
    if j-v < 0: continue
    dp[i][j] = min(w + dp[i-1][j-v], dp[i-1][j])

ans = 0

for i in range(110000):
  if dp[-1][i] > W: continue
  ans = max(ans, i)

print(ans)
# print(dp[-1][:100])
