N = int(input())
h = list(map(int, input().split()))
dp = [0] * N

for i in range(N-1):
  if(i == 0):
    dp[i+1] = dp[i] + abs(h[i] - h[i+1])
  else:
    dp[i+1] = min(dp[i] + abs(h[i] - h[i+1]), dp[i-1] + abs(h[i-1] - h[i+1]))

print(dp[-1])
