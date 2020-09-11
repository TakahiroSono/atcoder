A, B, C = map(int, input().split())
K = int(input())

count = 0
while not A < B:
  B *= 2
  count += 1
while not B < C:
  C *= 2
  count += 1

if count <= K and A < B < C:
  print('Yes')
else:
  print('No')
