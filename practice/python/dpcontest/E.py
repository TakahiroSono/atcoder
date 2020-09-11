N, W = map(int, input().split())
WV = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (W+1) for _ in range(N+1)]

for n in range(1, N+1):
  for w in range(W+1):
    if (w - WV[n-1][0] >= 0):
      dp[n][w] = max(dp[n-1][w], dp[n-1][w - WV[n-1][0]] + WV[n-1][1])
    else:
      dp[n][w] = dp[n-1][w]

print(dp[-1][-1])
