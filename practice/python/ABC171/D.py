N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]

indexA = {}

for a in A:
  if a not in indexA:
    indexA[a] = 0
  indexA[a] += 1

sumA = sum(A)

for (b,c) in BC:
  if b in indexA:
    sumA += (c-b) * indexA[b]
    if c not in indexA:
      indexA[c] = 0
    indexA[c] += indexA[b]
    indexA[b] = 0
  print(sumA)
