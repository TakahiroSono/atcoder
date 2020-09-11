k = int(input())
n = len(input())

MOD = 10**9 + 7

fact = [1] * 2200000
invfact = [1] * 2200000

for i in range(1, 2200000):
  fact[i] = fact[i-1] * i % MOD

invfact[-1] = pow(fact[-1], MOD-2, MOD)

for i in range(2200000-1, 0, -1):
  invfact[i-1] = invfact[i] * i % MOD

def nCk(n, k):
  return fact[n] * invfact[k] * invfact[n-k] % MOD

ans = 0

for l in range(n, n+k+1):
  ans += pow(25, l-n, MOD) * nCk(l-1,n-1) * pow(26, n+k-l, MOD) % MOD
  ans %= MOD

print(ans)
