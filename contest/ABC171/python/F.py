K = int(input())
S = input()
MOD = 10 ** 9 + 7

ls = len(S)
ans = 26 ** K % MOD

ans += K * ls
ans %= MOD

print(ans)
