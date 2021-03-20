N = int(input())

cnt = 0

for i in range(1, 10**6 + 100):
  num = int(str(i) + str(i))
  if num > N: break
  else:
    cnt += 1

print(cnt)
