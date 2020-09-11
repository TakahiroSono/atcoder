import math

N = int(input())
A = list(map(int, input().split()))
MOD = 10 ** 9 + 7

prime = list(range(1001))
prime[:2] = -1

for i in range(2, 1001):
  for j in range(i+i, 1001, i):
    prime[j] = i

print(prime)
