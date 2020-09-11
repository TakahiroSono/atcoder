H, W, K = map(int, input().split())
C = [input() for _ in range(H)]

total = 0

for i in range(2**(H)):
  for j in range(2**(W)):
    pattern = 0
    bin_H = '{:09b}'.format(i)[-H:]
    bin_W = '{:09b}'.format(j)[-W:]
    for hi,h in enumerate(bin_H):
      if h == '0':
        for wi,w in enumerate(bin_W):
          if w == '0' and C[hi][wi] == "#":
            pattern += 1
    if pattern == K:
      total += 1
print(total)
