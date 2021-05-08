from itertools import combinations

N = int(input())
A = list(map(int, input().split()))
mod_A = [a % 200 for a in A]

def same(b, c):
  for i in range(len(b), len(c)):
    if b[i] == c[i]:
      return False
  return True

mod_dict = {}
for i,a in enumerate(mod_A, 1):
  if a in mod_dict:
    print('Yes')
    print(1, *mod_dict[a])
    print(2, a)
    exit
  else:
    mod_dict[a] = [[i]]

for i in range(2, 200):
  for a in combinations(range(N), i):
    mod = sum([mod_A[j] for j in a]) % 200
    if mod in mod_dict:
      for j in range(len(mod_dict[mod])):
        if not same(a, mod_dict[mod][j]):
          print('Yes')
          print(1, *mod_dict[mod][j])
          print(2, *a)
          exit
    mod_dict[mod].append(a)

print('No')
