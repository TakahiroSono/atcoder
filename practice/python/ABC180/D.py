X, Y, A, B = map(int, input().split())
exp = 0

while X <= Y:
  if X * A < X + B:
    if X * A > Y: break
    X *= A
    exp += 1
  else:
    break

print(exp + (Y - X) // B - (not (Y - X) % B))
