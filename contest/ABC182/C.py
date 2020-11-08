from collections import Counter
N = list(map(int, list(input())))
sum_n = sum(N)

cnt_n = Counter(N)
remain = [0] * 3
remain_n = sum_n % 3

if remain_n:
  for k,v in cnt_n.items():
    remain[k % 3] += v
  if remain[remain_n]:
    print("1" if len(N) > 1 else "-1")
  else:
    if remain_n == 1:
      print("2" if remain[2] > 1 and len(N) > 2 else "-1")
      exit()
    if remain_n == 2:
      print("2" if remain[1] > 1 and len(N) > 2 else "-1")

else:
  print("0")
