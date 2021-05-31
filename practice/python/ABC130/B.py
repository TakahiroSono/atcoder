N, X = map(int, input().split())
L = list(map(int, input().split()))
bound = [0] * (N+1)

for i in range(1, N+1):
  bound[i] = bound[i-1] + L[i-1]

cnt = 0;
for i in range(N+1):
  if bound[i] <= X:
    cnt += 1

print(cnt)
