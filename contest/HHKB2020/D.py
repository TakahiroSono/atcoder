MOD = 10**9 + 7
T = int(input())

for _ in range(T):
  n, a, b = map(int, input().split())
  # a >= b
  a, b = max(a, b), min(a, b)
  # Aを敷き詰める
  a_max = (n - a + 1) ** 2
  # Bを敷き詰める
  b_max = (n - b + 1) ** 2
  # 敷き詰める重複あり
  all_max = a_max * b_max
  # 重複
  ## 角
  dup_sq = 4 * ((a - b + 1) ** 2)

  dup = () * (a + b - 1) ** 2
  print(a_max, b_max, dup)
  print((all_max - dup) % MOD)
