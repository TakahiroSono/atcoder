a, b, c = map(int, input().split())

if a == b:
  print(c)
  exit()
if b == c:
  print(a)
  exit()
if c == a:
  print(b)
  exit()

print(0)
