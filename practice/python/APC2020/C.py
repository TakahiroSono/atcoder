N = int(input())
sqn = int(N**0.5)
cnt = [0] * N*10
for x in range(1, sqn):
  for y in range(1, sqn):
    for z in range(1, sqn):
      cnt[x*x + y*y + z*z + x*y + y*z + z*x - 1] += 1

print('\n'.join(map(str, cnt[:N])))
