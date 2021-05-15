from itertools import product

S = input()
o = [i for i,s in enumerate(S) if s == 'o']
x = [i for i,s in enumerate(S) if s == 'x']
q = [i for i,s in enumerate(S) if s == '?']

if len(o) > 4:
  print(0)
  exit()

cnt = 0

for p in product(range(10), repeat=4):
  if len(set(p) & set(x)) > 0: continue
  if len(set(p) & set(o)) == len(o):
    cnt += 1

print(cnt)
