N,M,X = map(int, input().split())
books = [list(map(int, input().split())) for _ in range(N)]
buy = []

for i in range(1,2**(N+1)):
  bought = list(format(i, '0{}b'.format(N)))
  params = [0] * (M+1)
  for b, book in zip(bought, books):
    if b == '1':
      params = [pi+ai for pi,ai in zip(params,book)]
  for p in params[1:]:
    if p < X:
      break
  else:
    buy.append(params)

buy.sort()
print(buy[0][0] if len(buy) > 0 else -1)
