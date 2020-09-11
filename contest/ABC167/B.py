a,b,c,k = map(int, input().split())
if a >= k:
  print(k)
  exit()
if a+b >= k:
  print(a)
  exit()

print(a-(k-a-b))
