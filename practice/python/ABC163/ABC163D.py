# n,k=map(int,input().split())
# s=0
# for i in range(k,n+2):
#   s+=i*(n-i+1)+1
# print(s%(10**9+7))

import itertools as it

N,K = map(int, input().split())
mod = 10**9 + 7
left = it.islice(it.accumulate(reversed(range(N+1))), K-1, N+1)
right = it.islice(it.accumulate(range(N+1)), K-1, N+1)
ans = sum(map(lambda x,y: x-y+1, left, right))
print(ans%mod)
