N, K = map(int, input().split())
A = list(map(int, input().split()))
MOD = 10**9 + 7

sA = sorted(A, reverse=True)
pAb = [1]
pAs = [1]
mAb = [1]
mAs = [1]

for a, ra in zip(sA, sA[::-1]):
  if a >= 0:
    pAb.append(a)
    pAs.append(ra)
  else:
    mAb.append(abs(ra))
    mAs.append(abs(a))

for i in range(1, len(pAb)):
  pAb[i] *= pAb[i-1]
  pAs[i] *= pAs[i-1]

for i in range(2, len(mAb)):
  mAb[i] *= mAb[i-1]
  mAs[i] *= mAs[i-1]

ans = -float('inf')

for i in range(K+1):
  if len(pAb) > 1 and len(mAb) > 1:
    if len(pAb) < i or len(mAb) < K-i+1:
      break
    if K-i % 2:
      # odd
      print(i, len(pAs), len(mAs), K-i+1)
      ans = max(ans, pAs[i+1] * -mAs[K-i+1])
    else:
      # even
      ans = max(ans, pAb[i+1] * mAb[K-i+1])

if len(pAb) == 1:
  if K % 2:
    ans = max(ans, -mAs[K+1])
  else:
    ans = max(ans, -mAs[K+1])

if len(mAb) == 1:
  ans = max(ans, mAb[K+1])

print(ans % MOD)
