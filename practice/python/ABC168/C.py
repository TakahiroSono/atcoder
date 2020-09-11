import math

a, b, h, m = map(int, input().split())
# h: a, m: b

H =  ((h + m / 60) / 12) * (2 * math.pi)
M = (m / 60) * (2 * math.pi)

if M - H >= 0:
  print('{:.10f}'.format(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(M - H))))
else:
  print('{:.10f}'.format(math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(H - M))))
