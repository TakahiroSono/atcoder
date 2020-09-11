def nPk(n, k):
  return fact[n] * invfact[n-k] % MOD

def nCk(n, k):
  return fact[n] * invfact[k] * invfact[n-k] % MOD

N, M = map(int, input().split())
MOD = 10 ** 9 + 7

fact = [0] * 1100000
invfact = [0] * 1100000

fact[0] = 1

for i in range(1, 1100000):
  fact[i] = fact[i-1] * i % MOD

invfact[-1] = pow(fact[-1], MOD-2, MOD)

for i in range(1100000-1, 0, -1):
  invfact[i-1] = invfact[i] * i % MOD

ans = 0

for k in range(N + 1):
  temp = nCk(N, k) * nPk(M, k) * (nPk(M-k, N-k) ** 2) % MOD
  if k % 2 == 0:
    ans += temp
  else:
    ans -= temp
  ans %= MOD

print(ans)
