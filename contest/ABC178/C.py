N = int(input())
MOD = 10**9 + 7

fact = [0] * 1100000
invfact = [0] * 1100000

fact[0] = 1

if N < 2:
  print(0)
  exit()

for i in range(1, 1100000):
  fact[i] = fact[i-1] * i % MOD

invfact[-1] = pow(fact[-1], MOD-2, MOD)

for i in range(1100000-1, 0, -1):
  invfact[i-1] = invfact[i] * i % MOD

def nCk(n, k):
  return fact[n] * invfact[n-k] * invfact[k] % MOD

# print(N * (N-1) % MOD)
nk = nCk(N,2) * 2
print(((8 ** (N-2) * nk) + (2 ** N - 2)) % MOD)
