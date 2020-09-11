N,M = map(int, input().split())
A_sum = sum(map(int, input().split()))
total = N-A_sum
print(-1 if total < 0 else total)
