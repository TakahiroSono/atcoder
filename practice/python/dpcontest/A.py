# N = int(input())
# h = list(map(int, input().split()))
# dp = [0] * N

# for i in range(N-1):
#   if(i == 0):
#     dp[i+1] = dp[i] + abs(h[i] - h[i+1])
#   else:
#     dp[i+1] = min(dp[i] + abs(h[i] - h[i+1]), dp[i-1] + abs(h[i-1] - h[i+1]))

# print(dp[-1])

N = int(input())
H = list(map(int, input().split()))
cost = [float('inf')] * N
cost[0] = 0

for i in range(1, N):
  cost[i] = min(abs(H[i-1] - H[i]) + cost[i-1], cost[i])
  if i >= 2:
    cost[i] = min(abs(H[i-2] - H[i]) + cost[i-2], cost[i])

print(cost[-1])
print(cost)
