H, W = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(H):
  for j in range(W):
    if i+1 < H:
      ans += S[i][j] == "." and S[i+1][j] == "."
    if j+1 < W:
      ans += S[i][j] == "." and S[i][j+1] == "."

print(ans)
