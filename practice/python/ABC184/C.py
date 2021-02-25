from itertools import product

r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

def is_moved(a, b, c, d):
  if a + b == c + d: return True
  if a - b == c - d: return True
  if abs(a - c) + abs(b - d) <= 3: return True
  return False

if r1 == r2 and c1 == c2:
  print(0)
  exit()

if is_moved(r1, c1, r2, c2):
  print(1)
  exit()

for i, j in product(range(-4, 5), repeat=2):
  r3, c3 = r1 + i, c1 + j
  if is_moved(r1, c1, r3, c3) and is_moved(r3, c3, r2, c2):
    print(2)
    exit()

move = r2 + c2 - r1 - c1
if move % 2 == 0:
  print(2)
  exit()

print(3)
