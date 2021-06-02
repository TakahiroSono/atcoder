a, b = map(int, input().split())
A, B = a, b

if A < B :
  A, B = B, A

while B > 0:
  A, B = B, A % B


ans = (b // A) * a
print(ans)
