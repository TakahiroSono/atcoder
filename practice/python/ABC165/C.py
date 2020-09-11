from itertools import product
N, M, Q = map(int, input().split())

choice = []

for i in product([0, 1], repeat=(M)):
  if sum(i) == N:
    choice.append([j for ii,j in zip(i,range(1, M+1)) if ii == 1])

print(choice)
# for i in range(Q):
#   a, b, c, d = map(int, input().split())
#   for
