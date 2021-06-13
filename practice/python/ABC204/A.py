x, y = map(int, input().split())
ans = set([0,1,2])

if x != y:
  ans.remove(x)
  ans.remove(y)
  print(ans.pop())
else:
  print(x)
