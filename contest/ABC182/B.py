N = int(input())
A = list(map(int, input().split()))
gcd = [[0,i] for i in range(1100)]

for i in range(2, 1000):
  for a in A:
    if a % i:
      continue
    else:
      gcd[i][0] += 1

gcd.sort(reverse=True)
print(gcd[0][1])
