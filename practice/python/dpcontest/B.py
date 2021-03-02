# n, k = map(int, input().split())
# h = list(map(int, input().split()))

# dp = [float('inf')] * n
# dp[0] = 0

# for i in range(1, n):
#   for j in range(1, k+1):
#     if(i-j < 0):
#       break
#     dp[i] = min(dp[i], dp[i-j] + abs(h[i-j] - h[i]))

# print(dp[-1])

N, K = map(int, input().split())
H = list(map(int, input().split()))

dp = [float('inf')] * N
dp[0] = 0

for n in range(1, N):
  for k in range(1, K+1):
    if n-k < 0: break
    dp[n] = min(dp[n], dp[n-k] + abs(H[n] - H[n-k]))

print(dp[-1])
print(dp)
