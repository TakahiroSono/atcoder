N, K = map(int, input().split())

ans = sum(range(1, N+1)) * 100 * K + sum(range(1, K+1)) * N

print (ans)
