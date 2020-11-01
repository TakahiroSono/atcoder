N = int(input())
dig = [[[0,0]] * N for _ in range(N)]
p = []

for _ in range(N):
  x, y = map(int, input().split())
  p.append([x,y])

for i in range(N):
  x1, y1 = p[i]
  for j in range(N):
    x2, y2 = p[j]
    if x1 == x2:
      dig[i][j] = [float('inf'), 0]
      continue
    a = (y1 - y2) / (x1 - x2)
    b = y1 - a * x1
    dig[i][j] = [a, b]

for i in range(N):
  for j in range(N-1):
    if i == j: continue
    a, b = dig[i][j]
    for k in range(j+1, N):
      if i == k: continue
      ak, bk = dig[i][k]
      if a == ak and b == bk:
        print('Yes')
        exit()

print('No')
