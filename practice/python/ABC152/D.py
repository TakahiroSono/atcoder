N = int(input())

dp = [[0] * 9 for _ in range(9)]

for i in range(1, N+1):
  if i % 10 != 0:
    si = str(i)
    start = int(si[0])
    fin = int(si[-1])
    dp[start-2][fin-2] += 1

ans = 0
for i in range(9):
  for j in range(9):
    ans += dp[i][j] * dp[j][i]

print(ans)
