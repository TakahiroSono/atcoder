N = int(input())
*A, = map(int, input().split())
sort_A = sorted(A)
re_a = [0 for _ in range(N)]
result = 0

for a in sort_A:
  a_index = sort_A.index(a)
  max_dis = [0,0]

  for i in range(N):
    if 0 <= abs(a_index-i) and re_a[abs(a_index-i)] != 0:
      max_dis[0] = abs(a_index-i)
    if N > abs(a_index+i) and re_a[abs(a_index+i)] != 0:
      max_dis[1] = abs(a_index+i)

  result += a * abs(max(max_dis))
  target_index = a_index + max(max_dis) if max_dis.index(max(max_dis)) else a_index - max(max_dis)
  re_a[target_index] = a
  sort_A[a_index] = 0

print(result)
