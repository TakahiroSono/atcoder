a, b, w = map(int, input().split())

w *= 1000
min_cnt = w
max_cnt = -1
for i in range(1, w // a + 1):
  if a <= w / i <= b:
    min_cnt = min(i, min_cnt)
    max_cnt = max(i, max_cnt)

if max_cnt == -1:
  print("UNSATISFIABLE")
else:
  print(min_cnt, max_cnt)
