import sys
sys.setrecursionlimit(10000)

N, M = map(int, input().split())

route = [[] for _ in range(N + 1)]

for i in range(M):
  a, b = map(int, input().split())
  route[a].append(b)

def dfs(city):
  if done[city]: return
  done[city] = True
  for c in route[city]: dfs(c)

ans = 0

for i in range(1, N+1):
  done = [False] * (N+1)
  dfs(i)
  ans += sum(done)

print(ans)
