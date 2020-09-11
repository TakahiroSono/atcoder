N = int(input())
A = list(map(int, input().split()))
Q = int(input())
BC = [list(map(int, input().split())) for _ in range(Q)]
ans = [0] * Q
index_A = { a: 0 for a in set(A) }

for a in A:
  index_A[a] += 1

for bc in BC:
  if bc[0] in index_A:
    if bc[1] not in index_A:
      index_A[bc[1]] = 0
    index_A[bc[1]] += index_A[bc[0]]
    index_A[bc[0]] = 0
  ans = sum(map(lambda i: i[0]*i[1], index_A.items()))

print('\n'.join(ans))
