a,b,c,d = map(int, input().split())

isWin = False
while not isWin:
  if a <= 0 or c <= 0:
    if a <= 0 and c > 0:
      print('No')
      exit()
    else:
      print('Yes')
      exit()
  a -= d
  c -= b
