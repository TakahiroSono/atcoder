N, K = map(int, input().split())
friends = [list(map(int, input().split())) for _ in range(N)]

friends.sort()

ans = K
for f in friends:
  if ans >= f[0]:
    ans += f[1]

print(ans)
