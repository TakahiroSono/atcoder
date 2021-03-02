# N = int(input())
# H = [list(map(int, input().split())) for _ in range(N)]

# dp = [[0] * 3 for _ in range(N+1)]
# # 0: umi, 1: yama, 2: HW

# for i in range(1, N+1):
#   for place in range(3):
#     for place_y in range(3):
#       if (place == place_y): continue
#       dp[i][place] = max(
#         dp[i][place],
#         dp[i-1][place_y] + H[i-1][place]
#       )

# print(max(dp[-1]))

from itertools import product
N = int(input())
happy = [[0] * 3 for _ in range(N+1)]

for n in range(N):
  *move, = map(int, input().split())
  for i, j in product(range(3), repeat=2):
    if i == j: continue
    happy[n+1][i] = max(happy[n+1][i], happy[n][j] + move[i])

print(max(happy[-1]))
print(happy)
