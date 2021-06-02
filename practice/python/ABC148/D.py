N = int(input())
A = list(map(int, input().split()))

cnt = 1
ans = []

for a in A:
  if a == cnt:
    ans.append(a)
    cnt += 1

if cnt == 1:
  print(-1)
  exit()
print(N - len(ans))
