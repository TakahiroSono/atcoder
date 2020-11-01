N = int(input())
ans = []

for i in range(1, int(N ** 0.5) + 1):
  if N % i:
    continue
  else:
    ans.append(i)
    if i != N // i:
      ans.append(N // i)

ans.sort()
print(*ans)
