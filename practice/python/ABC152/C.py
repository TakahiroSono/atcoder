N = int(input())
P = list(map(int, input().split()))

minimum = N + 1
ans = 0

for i in range(N):
  if minimum >= P[i]:
    ans += 1
    minimum = P[i]

print(ans)
