H, N = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * (110000) for _ in range(N+1)]

dp[0][0] = float('inf')

for n in range(1, N+1):
  for h in range(H+1):
    a, b = ab[n-1]
    if h + a >= 110000: continue
    dp[n][h+a] = min(
      dp[n][h] + b,
      dp[n-1][h] + b,
    )
    if dp[n][h] == 0: dp[n][h] = float('inf')

print(dp[N][H])

for d in dp:
  print(d[:H+1])
