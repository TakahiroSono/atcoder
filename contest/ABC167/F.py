n = int(input())
stock = [0,0]
S = [input() for _ in range(n)]
S.sort()

for s in S:
  stock[0] += s.count('(')
  stock[1] += s.count(')')
  if stock[0] < stock[1]:
    print('No')
    exit()

print('Yes' if stock[0]==stock[1] else 'No')
