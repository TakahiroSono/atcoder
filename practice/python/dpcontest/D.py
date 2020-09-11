# N, W = map(int, input().split())
# W_V = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0] * (W+1) for _ in range(N+1)]

# for n in range(1, N+1):
#   for w in range(W+1):
#     dp[n][w] = dp[n-1][w]
#     if(w - W_V[n-1][0] >= 0):
#       dp[n][w] = max(dp[n][w], dp[n-1][w - W_V[n-1][0]] + W_V[n-1][1])

# print(dp[-1][-1])

import numpy as np

N, W = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]
dp = np.zeros(shape=W + 1, dtype=np.int64)

for weight, value in items:
    dp[weight:] = np.maximum(dp[weight:], dp[:-weight] + value)

print(dp[-1])
print(dp)
