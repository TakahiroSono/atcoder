K = int(input())
A, B = map(int, input().split())
count = 0
k = K
while k <= B:
  count += 1
  k = K * count
  if A <= k <= B:
    print('OK')
    break
else:
  print('NG')
