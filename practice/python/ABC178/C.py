N = int(input())
MOD = 10 ** 9 + 7
print((10**N % MOD - 9**N % MOD - 9**N % MOD + 8**N % MOD) % MOD)
