N, K = map(int, input().split())
A = list(map(int, input().split()))

for i in range(N - K):
  score_2 = A[i+K]
  score_1 = A[i]
  print('Yes' if score_1 < score_2 else 'No')
