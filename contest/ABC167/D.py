N,K = map(int, input().split())
A = list(map(int, input().split()))
graph = [0] * N
point = 1
count = 0
flag = True
while count < K:
  graph[point-1] += 1
  count += 1
  if flag and graph[point-1] >= 3:
    stock = K - sum(graph)-1
    stock2 = sum([1 for i in graph if i >= 2])
    K = (stock % stock2) + 1
    count = 0
    flag = False
  point = A[point-1]

print(point)
