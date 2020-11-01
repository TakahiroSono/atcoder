N = int(input())
X = list(map(int, input().split()))
m, u, t = 0, 0, 0

for x in X:
  abs_x = abs(x)
  m += abs_x
  u += abs_x * abs_x
  t = max(t, abs_x)

print(m)
print(u ** 0.5)
print(t)
