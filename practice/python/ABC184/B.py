N, X = map(int, input().split())
S = list(input())

for s in S:
  if s == "x":
    if X == 0:
      continue
    X -= 1
  else:
    X += 1

print(X)
