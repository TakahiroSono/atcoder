N = int(input())
*A, = map(int, input().split())
subordinate = [0 for _ in range(N)]

for a in A:
  subordinate[a-1] += 1

print('\n'.join(map(str,subordinate)))
