H, W = map(int, input().split())

A = [list(input()) for _ in range(H)]
dp = [[[0,0] for _ in range(W)] for _ in range(H)]

for i in range(H):
  for j in range(W):
    now = i + j
    if(i == j == 0): continue
    # Takahashi
    if now % 2:
      if i == 0:
        if A[i][j] == "+":
          dp[i][j] = [dp[i][j-1][0] + 1, dp[i][j-1][1]]
        else:
          dp[i][j] = [dp[i][j-1][0] - 1, dp[i][j-1][1]]
        continue
      if j == 0:
        if A[i][j] == "+":
          dp[i][j] = [dp[i-1][j][0] + 1, dp[i-1][j][1]]
        else:
          dp[i][j] = [dp[i-1][j][0] - 1, dp[i-1][j][1]]
        continue
      if dp[i][j-1][1] > dp[i-1][j][1]:
        if A[i][j] == "+":
          dp[i][j] = [dp[i][j-1][0] + 1, dp[i][j-1][1]]
        else:
          dp[i][j] = [dp[i][j-1][0] - 1, dp[i][j-1][1]]
      else:
        if A[i][j] == "+":
          dp[i][j] = [dp[i-1][j][0] + 1, dp[i-1][j][1]]
        else:
          dp[i][j] = [dp[i-1][j][0] - 1, dp[i-1][j][1]]
    else:
      # aoki
      if i == 0:
        if A[i][j] == "+":
          dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] + 1]
        else:
          dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] - 1]
        continue
      if j == 0:
        if A[i][j] == "+":
          dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + 1]
        else:
          dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] - 1]
        continue
      if dp[i][j-1][0] > dp[i-1][j][0]:
        if A[i][j] == "+":
          dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] + 1]
        else:
          dp[i][j] = [dp[i][j-1][0], dp[i][j-1][1] - 1]
      else:
        if A[i][j] == "+":
          dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] + 1]
        else:
          dp[i][j] = [dp[i-1][j][0], dp[i-1][j][1] - 1]

if dp[-1][-1][0] > dp[-1][-1][1]:
  print("Takahashi")
elif dp[-1][-1][0] < dp[-1][-1][1]:
  print("Aoki")
else:
  print("Draw")

for d in dp:
  print(d)
