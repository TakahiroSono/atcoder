# H, W = map(int, input().split())

# A = [list(input()) for _ in range(H)]
# dp = [[[0,0] for _ in range(W)] for _ in range(H)]

# for i in range(H):
#   for j in range(W):
#     now = i + j
#     if(i == j == 0): continue
#     # Takahashi
#     if now % 2:
#       if i == 0:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i][j-1][0] + 1, dp[i][j-1][1]]
#         else:
#           dp[i][j] = [dp[i][j-1][0] - 1, dp[i][j-1][1]]
#         continue
#       if j == 0:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i-1][j][0] + 1, dp[i-1][j][1]]
#         else:
#           dp[i][j] = [dp[i-1][j][0] - 1, dp[i-1][j][1]]
#         continue
#       if dp[i][j-1][1] > dp[i-1][j][1]:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i][j-1][0] + 1, dp[i][j-1][1]]
#         else:
#           dp[i][j] = [dp[i][j-1][0] - 1, dp[i][j-1][1]]
#       else:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i-1][j][0] + 1, dp[i-1][j][1]]
#         else:
#           dp[i][j] = [dp[i-1][j][0] - 1, dp[i-1][j][1]]
#     else:
#       # aoki
#       if i == 0:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] + 1]
#         else:
#           dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] - 1]
#         continue
#       if j == 0:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + 1]
#         else:
#           dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] - 1]
#         continue
#       if dp[i][j-1][0] > dp[i-1][j][0]:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] + 1]
#         else:
#           dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] - 1]
#       else:
#         if A[i][j] == "+":
#           dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + 1]
#         else:
#           dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] - 1]

# if dp[-1][-1][0] > dp[-1][-1][1]:
#   print("Takahashi")
# elif dp[-1][-1][0] < dp[-1][-1][1]:
#   print("Aoki")
# else:
#   print("Draw")

# for d in dp:
#   print(d)

# H, W = map(int, input().split())

# A = [list(input()) for _ in range(H)]
# dp = [[[0,0] for _ in range(W)] for _ in range(H)]

# def choice(p1, p2, i):
#   s1 = p1[0] - p1[1]
#   s2 = p2[0] - p2[1]
#   if i % 2:
#     if s1 > s2: return p1
#     else: return p2
#   else:
#     if s1 < s2: return p1
#     else: return p2

# for i in range(H):
#   for j in range(W):
#     now = i + j
#     point = 1 if A[i][j] == '+' else -1
#     p = choice(dp[i-1][j], dp[i][j-1], now)
#     if now == 0: continue
#     if now % 2:
#       # Takahashi
#       if i == 0: dp[i][j] = [dp[i][j-1][0] + point, dp[i][j-1][1]]
#       if j == 0: dp[i][j] = [dp[i-1][j][0] + point, dp[i-1][j][1]]
#       p[0] += point
#       dp[i][j] = p
#     else:
#       # Aoki
#       if i == 0: dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] + point]
#       if j == 0: dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + point]
#       p[1] += point
#       dp[i][j] = p


# if dp[-1][-1][0] > dp[-1][-1][1]:
#   print("Takahashi")
# elif dp[-1][-1][0] < dp[-1][-1][1]:
#   print("Aoki")
# else:
#   print("Draw")


H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]
dp = [[0] * W for _ in range(H)]

for i in range(H-1, -1, -1):
  for j in range(W-1, -1, -1):
    if i == H-1 and j == W-1: continue
    dp[i][j] = -float('inf')
    if i + 1 < H:
      point = 1 if A[i+1][j] == '+' else -1
      dp[i][j] = max(dp[i][j], -dp[i+1][j] + point)
    if j + 1 < W:
      point = 1 if A[i][j+1] == '+' else -1
      dp[i][j] = max(dp[i][j], -dp[i][j+1] + point)


if dp[0][0] > 0:
  print("Takahashi")
elif dp[0][0] < 0:
  print("Aoki")
else:
  print("Draw")

for d in dp:
  print(d)
