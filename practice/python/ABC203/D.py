N, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
med = []
for i in range(N-K+1):
  for j in range(N-K+1):
    if i+K > N or j+K > N: continue
    a_map = sum([a[j:j+K] for a in A[i:i+K]], [])
    a_map.sort()
    print(i,j,a_map)
    med.append(a_map[K**2 // 2 - 1 + bool(K**2 % 2)])

print(min(med))
print(med)
