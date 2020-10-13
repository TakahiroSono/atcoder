X, K, D = map(int, input().split())

near_num = abs(X) // D

if near_num < K:
  odd = abs(X) - (near_num + 1) * D
  even = abs(X) - (near_num) * D
  print(abs(odd) if (K - (near_num)) % 2 else abs(even))
else:
  print(abs(abs(X) - D * K))
